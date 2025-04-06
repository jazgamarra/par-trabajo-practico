from app import db

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(20), nullable=False)
    
    # representacion en texto del objeto generado 
    def __repr__(self):
        return f"<Proveedor {self.nombre}>"
