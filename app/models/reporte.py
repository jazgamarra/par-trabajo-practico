from app import db

class Reporte(db.Model):
    __tablename__ = 'reporte'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String, nullable=False)  # Corregido aquí
    fecha_inicio_plazo = db.Column(db.Date, nullable=False)  # Corregido aquí
    fecha_fin_plazo = db.Column(db.Date, nullable=False)  # Corregido aquí
    id_cliente = db.Column(db.Integer, nullable=False)  # Corregido aquí
    id_proveedor = db.Column(db.Integer, nullable=False)  # Corregido aquí
    id_producto = db.Column(db.Integer, nullable=False)  # Corregido aquí
    subtotal = db.Column(db.Integer, nullable=False)  # Corregido aquí
        
    # representación en texto del objeto generado 
    def __repr__(self):
        return f"<Reporte {self.descripcion}>"
