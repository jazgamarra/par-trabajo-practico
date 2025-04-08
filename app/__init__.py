from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()

    # Configuración para usar PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    # Registrar Rutas 
    from app.routes.producto import producto_bp
    from app.routes.proveedor import proveedor_bp
    from app.routes.cliente import cliente_bp
    from app.routes.factura import factura_bp
    from app.routes.reporte import reporte_bp
    
    app.register_blueprint(producto_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(factura_bp)
    app.register_blueprint(reporte_bp)

    return app
