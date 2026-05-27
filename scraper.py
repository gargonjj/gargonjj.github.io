import requests
import discogs_client
import json

DISCOGS_TOKEN = 'gpuhnUEHqtwyThcAbjXNQsEFDWjpHYkexPmmYCCk'
USER_AGENT = "MagaroWebDiscogs/0.1"
FORBBIDEN_CHAR = '('

artists = ['Oasis', 'Sabrina Carpenter', 'Arctic Monkeys', 'Laur', 'Team Grimoire', 'Akira Complex', 'Duki', 'XXXTENTACION', 'Ado']


url = 'https://api.discogs.com/database/search?q={artist}'


for artist in artists:
    target_url = url.format(artist = artist)
    response = requests.get(target_url)
    data = response.json()
    artist_name = data['results'][0]['title'] 
    if FORBBIDEN_CHAR in artist_name:
        print(artist_name.split(' ')[0])
    else:
        print(artist_name)


