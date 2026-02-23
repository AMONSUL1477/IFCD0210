from flask import Flask, redirect, url_for,render_template,request
from datetime import datetime
import json
import os

app = Flask(__name__)

DATOS = "datos.json"

PAISES = ['Argentina','México','España']
GENEROS = ['Hombre','Mujer','No definido']
HOBBIES = ['Leer','Deporte','Musica','Video juegos','Viajar']

@app.route('/',methods = ['POST','GET'])
def index():
    datos = {}

    if request.method == 'POST':
        datos = {
            'pais' : request.form.get('pais'),
            'genero' : request.form.get('genero'),
            'hobbies' : request.form.getlist('hobbies')
        }
        with open(DATOS, 'w', encoding='utf-8') as f:
            json.dump(datos,f,indent=4, ensure_ascii=False)

        with open(DATOS, 'r', encoding='utf-8') as f:
            datos = json.load(f)

    return render_template('home.html',paises=PAISES, generos=GENEROS, hobbies=HOBBIES, estado=datos)

@app.route('/cargar',methods=['POST','GET'])
def cargar():
    with open(DATOS, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    return render_template('home.html',paises=PAISES, generos=GENEROS, hobbies=HOBBIES, estado=datos)

