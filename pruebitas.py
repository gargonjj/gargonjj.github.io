import requests
import discogs_client
import json
from flask import Flask, render_template

artist_url = 'https://api.discogs.com/database/search?q={artist}'

artists = ['Oasis', 'Sabrina Carpenter', 'Daft Punk', 'Laur', 'Team Grimoire', 'Akira Complex', 'Duki', 'XXXTENTACION', 'Ado']


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

print(info_dump(artists[4]))