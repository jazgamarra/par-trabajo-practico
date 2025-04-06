from flask import Blueprint, request, jsonify
from app import db
from app.models.producto import Producto
from app.schemas.producto import ProductoSchema
from utils.auth import require_api_key

producto_bp = Blueprint('producto_bp', __name__)
producto_schema = ProductoSchema() # para un solo producto
productos_schema = ProductoSchema(many=True) # para un LISTA DE productos

#####################################################
# [GET] /producto 
#####################################################
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
    if request.args.get('id'):
        producto = Producto.query.get(request.args.get('id'))
        return producto_schema.jsonify(producto)
    productos = Producto.query.all()
    return productos_schema.jsonify(productos)

#####################################################
# [POST] /producto 
#####################################################
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

#####################################################
# [PUT] /producto 
#####################################################
@producto_bp.route('/productos/<int:id>', methods=['PUT'])
@require_api_key 
def actualizar_producto(id):
    """
    Actualizar producto
    ---
    tags:
      - Productos
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del producto a actualizar
        schema:
          type: integer
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
      200:
        description: Producto actualizado
    """
    data = request.json
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    producto_schema.load(data, instance=producto, session=db.session)
    db.session.commit()
    return producto_schema.jsonify(producto), 200

#####################################################
# [DELETE] /producto
#####################################################
@producto_bp.route('/productos/<int:id>', methods=['DELETE'])
@require_api_key
def eliminar_producto(id):
    """
    Eliminar producto
    ---
    tags:
      - Productos
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del producto a eliminar
        schema:
          type: integer
    responses:
      204:
        description: Producto eliminado
    """
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    db.session.delete(producto)
    db.session.commit()
    return '', 204
