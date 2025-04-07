from flask import Blueprint, request, jsonify
from app import db
from app.models.reporte import Reporte # modelo!!!!
from app.schemas.reporte import ReporteSchema
from utils.auth import require_api_key

reporte_bp = Blueprint('reporte_bp', __name__) 
reporte_schema = ReporteSchema() # para un solo reporte 
reportes_schema = ReporteSchema(many=True) # para un LISTA DE reporte

#####################################################
# [GET] /reporte
#####################################################
@reporte_bp.route('/reporte', methods=['GET'])
@require_api_key
def get_reporte():
    """
    Listar reportes
    ---
    tags:
      - Reportes
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: Lista de reportes, o datos de un solo reporte si se encuentra el id 
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  descripcion:
                    type: string
                  fecha_inicio_plazo:
                    type: date
                  fecha_fin_plazo:
                    type: date
                  id_cliente:
                    type: integer
                  id_proveedor:
                    type: integer
                  id_producto:
                    type: integer
                  subtotal:
                    type: integer                  
    """
    # Si se encuentra el id en la peticion 
    if 'id' in request.args:
        id = request.args['id']
        reporte = Reporte.query.get(id)
        if reporte:
            return reporte_schema.jsonify(reporte)
        else:
            return jsonify({'error': 'Reporte no encontrado'}), 404
        
    # Si no se encuentra el id, se devuelven todos los reportes
    reportes = Reporte.query.all()
    return reportes_schema.jsonify(reportes)

#####################################################
# [POST] /reporte
#####################################################
@reporte_bp.route('/reporte', methods=['POST'])
@require_api_key
def crear_reporte():
    """
    Crear reporte
    ---
    tags:
      - Reportes
    security:
      - ApiKeyAuth: []
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              descripcion:
                type: string
              fecha_inicio_plazo:
                type: date
              fecha_fin_plazo:
                type: date
              id_cliente:
                type: integer
              id_proveedor:
                type: integer
              id_producto:
                type: integer
              subtotal:
                type: integer
            required:
              - descripcion
              - fecha_inicio_plazo
              - fecha_fin_plazo
              - id_cliente
              - id_proveedor
              - id_producto
              - subtotal
    responses:
      201:
        description: Reporte creado
    """
    
    data = request.json # obtener el json del cuerpo de la peticion 
    nuevo_reporte = reporte_schema.load(data, session=db.session) 
    db.session.add(nuevo_reporte)
    db.session.commit()
    return reporte_schema.jsonify(nuevo_reporte), 201

@reporte_bp.route('/reporte/<int:id>', methods=['PUT'])
@require_api_key
def actualizar_reporte(id):
    """
    Actualizar reporte por ID
    ---
    tags:
      - Reportes
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del reporte a actualizar
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              descripcion:
                type: string
              fecha_inicio_plazo:
                type: date
              fecha_fin_plazo:
                type: date
              id_cliente:
                type: integer
              id_proveedor:
                type: integer
              id_producto:
                type: integer
              subtotal:
                type: integer
    responses:
      200:
        description: Reporte actualizado correctamente
      404:
        description: Reporte no encontrado
    """
    reporte = Reporte.query.get(id)
    if not reporte:
        return jsonify({'error': 'Reporte no encontrado'}), 404

    data = request.json
    reporte.descripcion = data.get('descripcion', reporte.descripcion) # actualizar solo si se proporciona uno nuevo en la peticion
    reporte.fecha_inicio_plazo = data.get('fecha_inicio_plazo',reporte.fecha_inicio_plazo)
    reporte.fecha_fin_plazo = data.get('fecha_fin_plazo',reporte.fecha_fin_plazo)
    reporte.id_cliente = data.get('id_cliente',reporte.id_cliente)
    reporte.id_proveedor = data.get('id_proveedor',reporte.id_proveedor)
    reporte.id_producto = data.get('id_producto',reporte.id_producto)
    reporte.subtotal = data.get('subtotal',reporte.subtotal)
    
    db.session.commit()
    return reporte_schema.jsonify(reporte), 200

@reporte_bp.route('/reporte/<int:id>', methods=['DELETE'])
@require_api_key
def eliminar_reporte(id):
    """
    Eliminar reporte por ID
    ---
    tags:
      - Reportes
    security:
      - ApiKeyAuth: []
    parameters:
      - name: id
        in: path
        required: true
        description: ID del reporte a eliminar
        schema:
          type: integer
    responses:
      204:
        description: Reporte eliminado correctamente
      404:
        description: Reporte no encontrado
    """
    reporte = Reporte.query.get(id)
    if not reporte:
        return jsonify({'error': 'Reporte no encontrado'}), 404

    db.session.delete(reporte)
    db.session.commit()
    return f'Reporte {id} eliminado', 204