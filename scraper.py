import requests
import discogs_client
import json
from flask import Flask, render_template

DISCOGS_TOKEN = 'gpuhnUEHqtwyThcAbjXNQsEFDWjpHYkexPmmYCCk'
USER_AGENT = "MagaroWebDiscogs/0.1"
FORBBIDEN_CHAR = '('

artists = ['Oasis', 'Sabrina Carpenter', 'Daft Punk']


artist_url = 'https://api.discogs.com/database/search?q={artist}'

app = Flask(__name__)


#Selects the first result of searching an artist name
def info_dump(artist: str) -> dict:
    target_url = artist_url.format(artist = artist)
    response = requests.get(target_url)
    data = response.json()
    artist_info = requests.get(data['results'][0]['resource_url'])
    return artist_info.json()

def get_profile_pic(artist: str) -> str:
    artist_info = info_dump(artist)
    profile_pic_url = artist_info['images'][0]['uri']
    return profile_pic_url

def get_artist_name(artist: str) -> str:
    artist_info = info_dump(artist)
    artist_name = artist_info['name']
    return artist_name
    

@app.route('/')
def inicio():
    title = 'Magaro'
    artists_data = {}
    for artist in artists:
        name = get_artist_name(artist)
        pic = get_profile_pic(artist)
        artists_data[name] = pic

    return render_template('index.html', main_title = title, artists_data = artists_data)

if __name__ == '__main__':
    app.run(debug=True)


