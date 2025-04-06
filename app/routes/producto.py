# app/routes/producto.py
from flask import Blueprint, request, jsonify
from app import db
from app.models.producto import Producto
from app.schemas.producto import ProductoSchema
from flasgger import swag_from

producto_bp = Blueprint('producto_bp', __name__)
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

@producto_bp.route('/productos', methods=['GET'])
def get_productos():
    """
    Listar productos
    ---
    tags:
      - Productos
    responses:
      200:
        description: Lista de productos
    """
    productos = Producto.query.all()
    return productos_schema.jsonify(productos)

@producto_bp.route('/productos', methods=['POST'])
def crear_producto():
    """
    Crear producto
    ---
    tags:
      - Productos
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Producto'
    responses:
      201:
        description: Producto creado
    """
    data = request.json
    nuevo_producto = producto_schema.load(data, session=db.session)
    db.session.add(nuevo_producto)
    db.session.commit()
    return producto_schema.jsonify(nuevo_producto), 201
