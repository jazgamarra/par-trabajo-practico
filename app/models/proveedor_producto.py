from app import db 
from app.models.proveedor import Proveedor
from app.models.producto import Producto
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Float, Boolean

class ProveedorProducto(db.Model):
    __tablename__ = 'proveedor_producto'
    id = Column(Integer, primary_key=True)
    proveedor_id = Column(Integer, ForeignKey('proveedor.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    precio = Column(Float, nullable=False)
    activo = Column(Boolean, default=True)

    proveedor = relationship('Proveedor', back_populates='proveedor_productos')
    producto = relationship('Producto', back_populates='proveedor_productos')

    def __repr__(self):
        return f'<ProveedorProducto {self.id}>'