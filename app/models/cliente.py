from app import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    # representacion en texto del objeto generado 
    def __repr__(self):
        return f"<Cliente {self.nombre}>"