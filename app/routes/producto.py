from flask import Blueprint, request, jsonify
from app import db
from app.models.producto import Producto
from app.schemas.producto import ProductoSchema
from utils.auth import require_api_key

producto_bp = Blueprint('producto_bp', __name__)
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

@producto_bp.route('/productos', methods=['GET'])
@require_api_key
def get_productos():
    """
    Listar productos
    ---
    tags:
      - Productos
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: Lista de productos
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  nombre:
                    type: string
                  precio:
                    type: number
                  descripcion:
                    type: string
    """

    productos = Producto.query.all()
    return productos_schema.jsonify(productos)

@producto_bp.route('/productos', methods=['POST'])
@require_api_key
def crear_producto():
    """
    Crear producto
    ---
    tags:
      - Productos
    security:
      - ApiKeyAuth: []
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nombre:
                type: string
              precio:
                type: number
              descripcion:
                type: string
            required:
              - nombre
              - precio
    responses:
      201:
        description: Producto creado
    """
    
    data = request.json
    nuevo_producto = producto_schema.load(data, session=db.session)
    db.session.add(nuevo_producto)
    db.session.commit()
    return producto_schema.jsonify(nuevo_producto), 201
