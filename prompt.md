Actúa como programador experto en Python, Flask, PostgreSQL y APIs REST.

Necesito un archivo Python llamado `scraper.py` para un proyecto de clase. El programa debe consumir la API de Discogs, buscar varios artistas, guardar sus datos y sus lanzamientos en PostgreSQL, y mostrarlos en una página web con Flask.

Requisitos:

- Usar `requests`, `psycopg2`, `Flask`, `datetime`, `webbrowser` y `Timer`.
- Conectarse a PostgreSQL con estos datos:
  host: 192.168.56.103
  database: Magaro 
  user: postgres
  password: 1234
  port: 5432

Tablas disponibles:

- `artists`: artist_id, discogs_artist_id, name, profile, profile_img
- `products`: product_id, discogs_product_id, title, artist_id, release_date, origin_url, img_url, last_update

Funcionamiento:

1. Buscar artistas en la API de Discogs.
2. Obtener sus datos principales: id, nombre, perfil, imagen y releases_url.
3. Insertar o actualizar el artista en la tabla `artists`.
4. Obtener hasta 10 lanzamientos por artista.
5. Guardar cada lanzamiento en `products`.
6. Usar `ON CONFLICT` para evitar duplicados.
7. Crear una ruta `/` con Flask que ejecute el scraping, consulte los productos y renderice `index.html`.
8. Enviar al template:
   - `main_title`
   - `products`
9. Abrir automáticamente el navegador en `http://127.0.0.1:5000`.

Lista de artistas:

- Oasis
- Sabrina Carpenter
- Daft Punk
- Laur
- Team Grimoire
- Akira Complex
- Duki
- XXXTENTACION
- Ado

El código debe estar en un solo archivo, sin clases, bien comentado y fácil de entender para estudiantes.
