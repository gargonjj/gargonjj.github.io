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
    con = psycopg2.connect(host= "192.168.56.103",
    database = "Magaro",
    user = "postgres",
    password = "1234",
    port = "5432"
    )
    cur = con.cursor()

def get_artists():

    query = 'SELECT * FROM artists'

def write_html():
    with open(FILE_PATH, 'w') as f:
        html_code = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Magaro</title>
    </head>
    <body>
        <div id="headerMenu">
            <img id="logo"/>
        </div>
        <div id="container">
            <div id="aboutUs">
                <div id="bigLogo"></div>
                <div id="aboutText"></div>
            </div>
            <div id="artists1">
                <div class="artistInfo">
                    <p>artist1</p>
                </div>
                <div class="artistInfo">
                    <p>artist2</p>
                </div>
                <div class="artistInfo">
                    <p>artist3</p>
                </div>
            </div>

            <div id="artists2">
                <div class="artistInfo">
                    <p>artist1</p>
                </div>
                <div class="artistInfo">
                    <p>artist2</p>
                </div>
                <div class="artistInfo">
                    <p>artist3</p>
                </div>
            </div>

            <div id="artists3">
                <div class="artistInfo">
                    <p>artist1</p>
                </div>
                <div class="artistInfo">
                    <p>artist2</p>
                </div>
                <div class="artistInfo">
                    <p>artist3</p>
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

write_html()