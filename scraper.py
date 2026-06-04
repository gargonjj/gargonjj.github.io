import os
import requests
from flask import Flask, render_template
import psycopg2
from datetime import datetime
import webbrowser 
from threading import Timer 

DISCOGS_TOKEN = 'gpuhnUEHqtwyThcAbjXNQsEFDWjpHYkexPmmYCCk'
USER_AGENT = "MagaroWebDiscogs/0.1"
FORBBIDEN_CHAR = '('

DB_PARAMS = {
    "host": "192.168.56.103",
    "database": "Magaro",
    "user": "postgres",
    "password": "1234",
    "port": 5432
}

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(**DB_PARAMS)

def clean_artist_name(name: str) -> str:
    if FORBBIDEN_CHAR in name:
        return name.split(FORBBIDEN_CHAR)[0].strip()
    return name.strip()

def scrape_and_insert_artist_products(artist_query: str):
    headers = {'User-Agent': USER_AGENT}
    search_url = f'https://api.discogs.com/database/search?q={artist_query}&type=artist&token={DISCOGS_TOKEN}'



    conn = None
    try:
        
        conn = get_db_connection()
        cur = conn.cursor()

        res = requests.get(search_url, headers=headers)
        res.raise_for_status()

        search_data = res.json()
        search_results = search_data.get('results', [])

        if not search_results:
            return

        first_result = search_results[0]
        artist_resource_url = first_result.get('resource_url')

        if not artist_resource_url:
            return



        artist_res = requests.get(f"{artist_resource_url}?token={DISCOGS_TOKEN}", headers=headers)
        artist_res.raise_for_status()
        artist_data = artist_res.json()

        discogs_artist_id = artist_data.get('id')
        raw_name = artist_data.get('name', artist_query)
        artist_name = clean_artist_name(raw_name)
        profile_text = artist_data.get('profile', '')
        images_list = artist_data.get('images', [])
        profile_img = images_list[0].get('uri', '') if images_list else ''




        cur.execute("""
            INSERT INTO artists (discogs_artist_id, name, profile, profile_img)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (discogs_artist_id) DO UPDATE 
            SET name = EXCLUDED.name, profile = EXCLUDED.profile
            RETURNING artist_id;
        """, (discogs_artist_id, artist_name, profile_text, profile_img))

        artist_id_row = cur.fetchone()
        if not artist_id_row:
            cur.execute("SELECT artist_id FROM artists WHERE discogs_artist_id = %s;", (discogs_artist_id,))
            artist_id = cur.fetchone()[0]
        else:
            artist_id = artist_id_row[0]



        releases_url = artist_data.get('releases_url')


        releases_res = requests.get(f"{releases_url}?token={DISCOGS_TOKEN}", headers=headers)
        print(f"[DEBUG] Respuesta HTTP releases: {releases_res.status_code}", flush=True)
        releases_res.raise_for_status()
        releases = releases_res.json().get('releases', [])
        print(f"[DEBUG] Total de lanzamientos recibidos: {len(releases)}", flush=True)


        for i, rel in enumerate(releases[:10]):
            title = rel.get('title', 'Unknown Title')
            discogs_prod_id = rel.get('id')

            genres_data = rel.get('genre', []) or rel.get('style', [])
            if isinstance(genres_data, list) and genres_data:
                genre_name = genres_data[0].strip()
            elif isinstance(genres_data, str) and genres_data:
                genre_name = genres_data.strip()
            else:
                genre_name = 'Otros'
            
            genre_name = genre_name[:50]

            raw_format = rel.get('format', '')
            if raw_format:
                format_name = raw_format.split(',')[0].strip()
            else:
                format_name = 'Desconocido'
            
            format_name = format_name[:30]
            

            img_url = rel.get('thumb', '')
            origin_url = f"https://www.discogs.com/release/{discogs_prod_id}"

            release_year = rel.get('year')
            try:
                release_date = (int(release_year))
            except:
                release_date = None

            cur.execute("""
                INSERT INTO products (discogs_product_id, title, artist_id, release_date, origin_url, img_url)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (discogs_product_id) DO UPDATE
                SET title = EXCLUDED.title, last_update = CURRENT_TIMESTAMP;
            """, (discogs_prod_id, title, artist_id,release_date, origin_url, img_url))
                

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        if conn:
            conn.rollback()
            conn.close()


@app.route('/')
def inicio():
    artists_to_scrape = ['Oasis', 'Sabrina Carpenter', 'Daft Punk', 'Laur', 'Team Grimoire', 'Akira Complex', 'Duki', 'XXXTENTACION', 'Ado']

    for artist in artists_to_scrape:
        scrape_and_insert_artist_products(artist)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.title, a.name, g.name, f.name, p.img_url 
        FROM products p
        JOIN artists a ON p.artist_id = a.artist_id
        LEFT JOIN genres g ON p.genre_id = g.genre_id
        LEFT JOIN formats f ON p.format_id = f.format_id
        ORDER BY p.last_update DESC;
    """)
    db_products = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('index.html', main_title='Magaro Shop', products=db_products)


def trigger_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1.2, trigger_browser).start()

    app.run(debug=True)

1