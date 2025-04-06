from app import ma
from app.models.proveedor import Proveedor

class ProveedorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =  Proveedor 
        load_instance = True 
