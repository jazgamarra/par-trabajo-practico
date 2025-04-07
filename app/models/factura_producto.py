from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class FacturaProducto(db.Model):
    __tablename__ = 'factura_producto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('producto.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    subtotal = Column(Integer, nullable=False)
    fact_prod = relationship('Producto', backref='factura_producto') 