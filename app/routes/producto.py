# app/routes/producto.py
from flask import Blueprint, request, jsonify
from app import db
from app.models.producto import Producto
from app.schemas.producto import ProductoSchema

producto_bp = Blueprint('producto_bp', __name__)
producto_schema = ProductoSchema() # para un solo producto
productos_schema = ProductoSchema(many=True) # para una lista de productos

# listar todos los productos 
@producto_bp.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return productos_schema.jsonify(productos)

# crear un nuevo producto
@producto_bp.route('/productos', methods=['POST'])
def crear_producto():
    data = request.json # obtiene los datos del request en json 

    # se valida y agrega el producto a la bd 
    nuevo_producto = producto_schema.load(data, session=db.session)
    db.session.add(nuevo_producto) 
    db.session.commit()
    
    return producto_schema.jsonify(nuevo_producto), 201
