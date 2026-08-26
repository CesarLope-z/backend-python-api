# Como primera instancia instalar flask
# pip install flask

from flask import Flask

app = Flask(__name__)

jugadores = [
        {"id": 1, "nombre": "Duri"},
        {"id": 2, "nombre": "Cesar"},
        {"id": 3, "nombre": "Diego"},
        {"id": 4, "nombre": "Ana"},
    ]

@app.route('/api/usuarios', methods=['GET'])
def obtener_jugadores():
    return {"jugadores": jugadores}

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def obtener_jugador_por_id(id):
   for jugador in jugadores:
        if jugador["id"] == id:
            return jugador

@app.route('/api/usuarios/<nombre>', methods=['GET'])
def obtener_jugador_por_nombre(nombre):
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            return jugador
