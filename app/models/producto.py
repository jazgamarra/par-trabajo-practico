from app import db

class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)

    proveedor_productos = db.relationship('ProveedorProducto', back_populates='producto', cascade='all, delete-orphan')
    factura_productos = db.relationship('FacturaProducto', back_populates='producto', cascade='all, delete-orphan')

    # representacion en texto del objeto generado 
    def __repr__(self):
        return f"<Producto {self.nombre}>"
