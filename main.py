# Como primera instancia instalar flask
# pip install flask

from flask import Flask

app = Flask(__name__)

usuarios = [
        {"id": 1, "nombre": "Duri"},
        {"id": 2, "nombre": "Cesar"},
        {"id": 3, "nombre": "Diego"},
        {"id": 4, "nombre": "Ana"},
    ]

@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return {"usuarios": usuarios}

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def obtener_usuario_por_id(id):
   for usuario in usuarios:
        if usuario["id"] == id:
            return usuario

@app.route('/api/usuarios/<nombre>', methods=['GET'])
def obtener_usuario_por_nombre(nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario
