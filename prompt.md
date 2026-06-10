Prompt for Automatic Scraping
Act as an AI agent specialized in API consumption and database management.
I need you to execute a complete scraping of the Discogs API following these requirements:
Database Configuration

Host: 192.168.56.103
Database: Magaro
User: postgres
Password: 1234
Port: 5432

Tables

artists: artist_id, discogs_artist_id, name, profile, profile_img
products: product_id, discogs_product_id, title, artist_id, release_date, origin_url, img_url, last_update

Execution Flow

For each artist in this list, perform a search in the Discogs API:

Oasis, Sabrina Carpenter, Daft Punk, Laur, Team Grimoire, Akira Complex, Duki, XXXTENTACION, Ado


For each artist found:

Extract: id, name, profile, profile image, releases URL
Insert or update in artists (use ON CONFLICT to avoid duplicates)


For each artist:

Get up to 10 releases from their releases URL
Extract: product id, title, release date, origin URL, image
Insert into products with reference to artist_id (use ON CONFLICT)


Error Handling:

If database connection fails, retry
If API has rate limit, wait and retry
Log any errors but continue with the next artist


Final Result:

Return a summary with:

Number of artists processed
Number of products saved
Errors encountered





Use only available tools to connect to PostgreSQL, make HTTP requests, and process JSON data.
