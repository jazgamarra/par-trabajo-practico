from flask import Blueprint, request, jsonify
from app import db
from app.models.proveedor import Proveedor # modelo!!!!
from app.schemas.proveedor import ProveedorSchema
from utils.auth import require_api_key

proveedor_bp = Blueprint('proveedor_bp', __name__) 
proveedor_schema = ProveedorSchema() # para un solo proveedor 
proveedores_schema = ProveedorSchema(many=True) # para un LISTA DE proveedor

#####################################################
# [GET] /proveedor
#####################################################
@proveedor_bp.route('/proveedor', methods=['GET'])
@require_api_key
def get_proveedor():
    """
    Listar proveedores
    ---
    tags:
      - Proveedores
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: Lista de proveedores, o datos de un solo proveedor si se encuentra el id 
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
                  contacto:
                    type: string
    """
    # Si se encuentra el id en la peticion 
    if 'id' in request.args:
        id = request.args['id']
        proveedor = Proveedor.query.get(id)
        if proveedor:
            return proveedor_schema.jsonify(proveedor)
        else:
            return jsonify({'error': 'Proveedor no encontrado'}), 404
        
    # Si no se encuentra el id, se devuelven todos los proveedores
    proveedores = Proveedor.query.all()
    return proveedores_schema.jsonify(proveedores)

#####################################################
# [GET] /proveedor
#####################################################
@proveedor_bp.route('/proveedor', methods=['POST'])
@require_api_key
def crear_proveedor():
    """
    Crear proveedor
    ---
    tags:
      - Proveedores
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
              contacto:
                type: string
            required:
              - nombre
              - contacto
    responses:
      201:
        description: Proveedor creado
    """
    
    data = request.json # obtener el json del cuerpo de la peticion 
    nuevo_proveedor = proveedor_schema.load(data, session=db.session) 
    db.session.add(nuevo_proveedor)
    db.session.commit()
    return proveedor_schema.jsonify(nuevo_proveedor), 201

@proveedor_bp.route('/proveedor/<int:id>', methods=['PUT'])
@require_api_key
def actualizar_proveedor(id):
    """
    Actualizar proveedor por ID
    ---
    tags:
      - Proveedores
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del proveedor a actualizar
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
              contacto:
                type: string
    responses:
      200:
        description: Proveedor actualizado correctamente
      404:
        description: Proveedor no encontrado
    """
    proveedor = Proveedor.query.get(id)
    if not proveedor:
        return jsonify({'error': 'Proveedor no encontrado'}), 404

    data = request.json
    proveedor.nombre = data.get('nombre', proveedor.nombre) # actualizar solo si se proporciona uno nuevo en la peticion
    proveedor.contacto = data.get('contacto', proveedor.contacto)
    
    db.session.commit()
    return proveedor_schema.jsonify(proveedor), 200

@proveedor_bp.route('/proveedor/<int:id>', methods=['DELETE'])
@require_api_key
def eliminar_proveedor(id):
    """
    Eliminar proveedor por ID
    ---
    tags:
      - Proveedores
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del proveedor a eliminar
        schema:
          type: integer
    responses:
      204:
        description: Proveedor eliminado correctamente
      404:
        description: Proveedor no encontrado
    """
    proveedor = Proveedor.query.get(id)
    if not proveedor:
        return jsonify({'error': 'Proveedor no encontrado'}), 404

    db.session.delete(proveedor)
    db.session.commit()
    return f'Proveedor {id} eliminado', 204
