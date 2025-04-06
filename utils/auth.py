# app/utils/auth.py
from flask import request, jsonify
from functools import wraps

API_KEY = "PAR_2025" 
# es la clave de API que se usara para autenticar las peticiones 
# deberia almacenarse como una variable de entorno o en un archivo de configuracion

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != f"Bearer {API_KEY}":
            return jsonify({"error": "No autorizado"}), 401
        return f(*args, **kwargs)
    return decorated
