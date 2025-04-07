from app import db

class Reporte(db.Model):
    __tablename__ = 'reporte'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String, nullable=False)
    fecha_inicio_plazo = db.Column(db.Date, nullable=False)
    fecha_fin_plazo = db.Column(db.Date, nullable=False)
    id_cliente = db.Column(db.Integer, nullable=True)
    id_proveedor = db.Column(db.Integer, nullable=True)
    id_producto = db.Column(db.Integer, nullable=True)
    subtotal = db.Column(db.Integer, nullable=False)
        
    # representación en texto del objeto generado 
    def __repr__(self):
        return f"<Reporte {self.descripcion}>"
