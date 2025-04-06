from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flasgger import Swagger 
from utils.swagger_template import template
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trabajopractico.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    # Registrar Rutas 
    from app.routes.producto import producto_bp
    from app.routes.proveedor import proveedor_bp
    from app.routes.cliente import cliente_bp
    
    app.register_blueprint(producto_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(cliente_bp)

    # Inicializar Swagger
    swagger = Swagger(app, template=template)

    return app
