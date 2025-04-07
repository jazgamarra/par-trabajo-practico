from flask import Blueprint, request, jsonify
from app import db
from app.models.factura import Factura # modelo!!!!
from app.schemas.factura import FacturaSchema
from utils.auth import require_api_key

factura_bp = Blueprint('factura_bp', __name__) 
factura_schema = FacturaSchema() # para un solo factura 
facturas_schema = FacturaSchema(many=True) # para un LISTA DE factura

#####################################################
# [GET] /factura
#####################################################
@factura_bp.route('/factura', methods=['GET'])
@require_api_key
def get_factura():
    """
    Listar facturas
    ---
    tags:
      - Facturas
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: Lista de facturas, o datos de un solo factura si se encuentra el id 
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  id_cliente:
                    type: integer
                  numero:
                    type: integer
                  total:
                    type: integer
    """
    # Si se encuentra el id en la peticion 
    if 'id' in request.args:
        id = request.args['id']
        factura = Factura.query.get(id)
        if factura:
            return factura_schema.jsonify(factura)
        else:
            return jsonify({'error': 'Factura no encontrado'}), 404
        
    # Si no se encuentra el id, se devuelven todos los facturas
    facturas = Factura.query.all()
    return facturas_schema.jsonify(facturas)

#####################################################
# [POST] /factura
#####################################################
@factura_bp.route('/factura', methods=['POST'])
@require_api_key
def crear_factura():
    """
    Crear factura
    ---
    tags:
      - Facturas
    security:
      - ApiKeyAuth: []
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:             
              id_cliente:
                type: integer
              numero:
                type: integer
              total:
                type: integer
            required:
              - id_cliente
              - numero
              - total
    responses:
      201:
        description: Factura creado
    """
    
    data = request.json # obtener el json del cuerpo de la peticion 
    nuevo_factura = factura_schema.load(data, session=db.session) 
    db.session.add(nuevo_factura)
    db.session.commit()
    return factura_schema.jsonify(nuevo_factura), 201

@factura_bp.route('/factura/<int:id>', methods=['PUT'])
@require_api_key
def actualizar_factura(id):
    """
    Actualizar factura por ID
    ---
    tags:
      - Facturas
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del factura a actualizar
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:                
              id_cliente:
                type: integer
              numero:
                type: integer
              total:
                type: integer
    responses:
      200:
        description: Factura actualizado correctamente
      404:
        description: Factura no encontrado
    """
    factura = Factura.query.get(id)
    if not factura:
        return jsonify({'error': 'Factura no encontrado'}), 404

    data = request.json
    factura.id_cliente = data.get('id_cliente', factura.id_cliente) # actualizar solo si se proporciona uno nuevo en la peticion
    factura.numero = data.get('numero',factura.numero)
    factura.total = data.get('precio',factura.total)
    
    db.session.commit()
    return factura_schema.jsonify(factura), 200

@factura_bp.route('/factura/<int:id>', methods=['DELETE'])
@require_api_key
def eliminar_factura(id):
    """
    Eliminar factura por ID
    ---
    tags:
      - Facturas
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del factura a eliminar
        schema:
          type: integer
    responses:
      204:
        description: Factura eliminado correctamente
      404:
        description: Factura no encontrado
    """
    factura = Factura.query.get(id)
    if not factura:
        return jsonify({'error': 'Factura no encontrado'}), 404

    db.session.delete(factura)
    db.session.commit()
    return f'Factura {id} eliminado', 204