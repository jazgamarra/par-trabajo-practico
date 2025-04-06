from flask import Blueprint, request, jsonify
from app import db
from app.models.cliente import Cliente # modelo!!!!
from app.schemas.cliente import ClienteSchema
from utils.auth import require_api_key

cliente_bp = Blueprint('cliente_bp', __name__) 
cliente_schema = ClienteSchema() # para un solo cliente 
clientes_schema = ClienteSchema(many=True) # para un LISTA DE cliente

#####################################################
# [GET] /cliente
#####################################################
@cliente_bp.route('/cliente', methods=['GET'])
@require_api_key
def get_cliente():
    """
    Listar clientes
    ---
    tags:
      - Clientes
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: Lista de clientes, o datos de un solo cliente si se encuentra el id 
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
                  email:
                    type: string
                  direccion:
                    type: string
                  telefono:
                    type: string
    """
    # Si se encuentra el id en la peticion 
    if 'id' in request.args:
        id = request.args['id']
        cliente = Cliente.query.get(id)
        if cliente:
            return cliente_schema.jsonify(cliente)
        else:
            return jsonify({'error': 'Cliente no encontrado'}), 404
        
    # Si no se encuentra el id, se devuelven todos los clientes
    clientes = Cliente.query.all()
    return clientes_schema.jsonify(clientes)

#####################################################
# [POST] /cliente
#####################################################
@cliente_bp.route('/cliente', methods=['POST'])
@require_api_key
def crear_cliente():
    """
    Crear cliente
    ---
    tags:
      - Clientes
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
              email:
                type: string
              direccion:
                type: string
              telefono:
                type: string
            required:
              - nombre
              - email
              - direccion
              - telefono
    responses:
      201:
        description: Cliente creado
    """
    
    data = request.json # obtener el json del cuerpo de la peticion 
    nuevo_cliente = cliente_schema.load(data, session=db.session) 
    db.session.add(nuevo_cliente)
    db.session.commit()
    return cliente_schema.jsonify(nuevo_cliente), 201

@cliente_bp.route('/cliente/<int:id>', methods=['PUT'])
@require_api_key
def actualizar_cliente(id):
    """
    Actualizar cliente por ID
    ---
    tags:
      - Clientes
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del cliente a actualizar
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
              email:
                type: string
              direccion:
                type: string
              telefono:
                type: string
    responses:
      200:
        description: Cliente actualizado correctamente
      404:
        description: Cliente no encontrado
    """
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({'error': 'Cliente no encontrado'}), 404

    data = request.json
    cliente.nombre = data.get('nombre', cliente.nombre) # actualizar solo si se proporciona uno nuevo en la peticion
    cliente.email = data.get('email', cliente.email)
    cliente.direccion = data.get('direccion', cliente.direccion)
    cliente.telefono = data.get('telefono', cliente.telefono)
    
    db.session.commit()
    return cliente_schema.jsonify(cliente), 200

@cliente_bp.route('/cliente/<int:id>', methods=['DELETE'])
@require_api_key
def eliminar_cliente(id):
    """
    Eliminar cliente por ID
    ---
    tags:
      - Clientes
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del cliente a eliminar
        schema:
          type: integer
    responses:
      204:
        description: Cliente eliminado correctamente
      404:
        description: Cliente no encontrado
    """
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({'error': 'Cliente no encontrado'}), 404

    db.session.delete(cliente)
    db.session.commit()
    return f'Cliente {id} eliminado', 204
