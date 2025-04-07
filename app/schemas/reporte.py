from app import ma
from app.models.reporte import Reporte

class ReporteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =  Reporte 
        load_instance = True 
