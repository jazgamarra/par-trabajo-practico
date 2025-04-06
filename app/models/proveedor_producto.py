from app import db 
from app.models import Proveedor, Producto
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Float, Boolean

class ProveedorProducto(db.Model):
    __tablename__ = 'proveedor_producto'
    id = Column(Integer, primary_key=True)
    proveedor_id = Column(Integer, ForeignKey('proveedor.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('producto.id'), nullable=False)
    precio = Column(Float, nullable=False)
    activo = Column(Boolean, default=True)

    proveedor = relationship(Proveedor, back_populates='productos')
    producto = relationship(Producto, back_populates='proveedores')

    def __repr__(self):
        return f'<ProveedorProducto {self.id}>'