import os
import requests
from flask import Flask, render_template
import psycopg2
from datetime import datetime
import webbrowser 
from threading import Timer

DB_PARAMS = {
    "host": "192.168.56.103",
    "database": "Magaro",
    "user": "postgres",
    "password": "1234",
    "port": 5432
}
FILE_PATH = 'templates/index.html'

def get_db_connection():
    con = psycopg2.connect(**DB_PARAMS)
    return con    

def get_artists(con):
    cur = con.cursor()
    query = 'SELECT * FROM artists'
    cur.execute(query)
    artists = cur.fetchall()
    print(artists)
    cur.close()
    return artists

def get_artists_names(artists):
    artists_names = []
    for artist in artists:
        artists_names.append(artist[2])
    return artists_names

def get_pic_urls(artists):
    pic_urls = []
    for artist in artists:
        pic_urls.append(artist[-1])
    return pic_urls


def write_html(artists_names: list, pic_urls: list):
    with open(FILE_PATH, 'w') as f:
        html_code = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Victor+Mono:wght@600&display=swap" rel="stylesheet">
        <title>Magaro</title>
    </head>
    <body>
        <div id="headerMenu">
            <img id="logo"/>
        </div>
        <div id="container">
            <div id="aboutUs">
                <div id="bigLogo"></div>
                <div id="aboutText">
                    <p id="about"><span style="font-style: italic">Magaro</span> is a fan-driven space for monthly music recomendations based in personal tastes</p>
                </div>
            </div>
            <div id="artists1">
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[0]}">
                    </div>
                    <p class="artistName">{artists_names[0]}</p>
                </div>
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[1]}">
                    </div>
                    <p class="artistName">{artists_names[1]}</p>
                </div>
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[2]}">
                    </div>
                    <p class="artistName">{artists_names[2]}</p>
                </div>
            </div>

            <div id="artists2">
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[3]}">
                    </div>
                    <p class="artistName">{artists_names[3]}</p>
                </div>
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[4]}">
                    </div>
                    <p class="artistName">{artists_names[4]}</p>
                </div>
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[5]}">
                    </div>
                    <p class="artistName">{artists_names[5]}</p>
                </div>
            </div>

            <div id="artists3">
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[6]}">
                    </div>
                    <p class="artistName">{artists_names[6]}</p>
                </div>
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[7]}">
                    </div>
                    <p class="artistName">{artists_names[7]}</p>
                </div>
                <div class="artistInfo">
                    <div class="picContainer">
                        <img class="artistPic" src="{pic_urls[8]}">
                    </div>
                    <p class="artistName">{artists_names[8]}</p>
                </div>
            </div>
        </div>
        <div id="footer">
            <p>
                Magaro es un proyecto académico.
                <br>
                Los derechos de los contenidos mostrados quedan reservados a sus propetarios.
            </p>
        </div>
    </body>
</html>
"""
        f.write(html_code)

#write_html()
get_db_connection()