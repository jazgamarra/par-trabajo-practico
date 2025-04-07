from app import ma
from app.models.factura import Factura
from app.models.cliente import Cliente

class FacturaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =  Factura # definimos que este esquema es para factura
        load_instance = True # permite convertir json a objetos de la clase factura
