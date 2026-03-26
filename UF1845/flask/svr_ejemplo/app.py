from flask import Flask, jsonify

app = Flask(__name__)

usuarios = {
    1: {"nombre":"Paco", "edad": 44},
    2: {"nombre":"Ana", "edad": 22},
}

@app.route('/usuarios/<int:id_usuario>') 
def obtener_usr(id_usuario):
    usuario = usuarios.get(id_usuario)
    return jsonify(usuario)

