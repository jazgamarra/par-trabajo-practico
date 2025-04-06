from app import ma
from app.models.cliente import Cliente

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =  Cliente 
        load_instance = True 
