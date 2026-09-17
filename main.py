# Como primera instancia instalar flask
# pip install flask

from flask import Flask, jsonify, request
from db import supabase
app = Flask(__name__)

@app.route('/api/jugadores', methods=['GET'])
def obtener_usuarios():
    try:
        response = supabase.table('jugadores').select('*').execute()
        return jsonify({"jugadores": response.data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST: Crear un nuevo jugador
@app.route('/api/jugadores', methods=['POST'])
def crear_jugador():
    try:
        data = request.json
        
        nombre = data.get('nombre')
        estilo = data.get('estilo')

        if not nombre:
            return jsonify({"error": "El campo 'nombre' es requerido"}), 400

        nuevo_jugador = {
            "nombre": nombre,
            "estilo": estilo
        }

        response = supabase.table('jugadores').insert(nuevo_jugador).execute()
        
        return jsonify(response.data[0]), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/jugadores/<int:id>', methods=['GET'])
def obtener_jugador_por_id(id):
    try:
        response = supabase.table('jugadores').select('*').eq('id', id).execute()
        if response.data:
            return jsonify({"jugador": response.data[0]}), 200
        else:
            return jsonify({"error": "Jugador no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Eliminar un jugador
@app.route('/api/jugadores/<int:id>', methods=['DELETE'])
def eliminar_jugador(id):
    try:
        
        response = supabase.table('jugadores').delete().eq('id', id).execute()
        
        if len(response.data) > 0:
            return jsonify({
                "mensaje": "Jugador eliminado correctamente", 
                "jugador_eliminado": response.data[0]
            }), 200
            
        return jsonify({"error": "Jugador no encontrado"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500