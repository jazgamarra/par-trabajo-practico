from app import db
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.factura import Factura
from app.models.producto import Producto 

class FacturaProducto(db.Model):
    __tablename__ = 'factura_producto'
    
    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, ForeignKey('facturas.id'), nullable=False)
    producto_id = db.Column(db.Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

    factura = relationship('Factura', back_populates='factura_productos')
    producto = relationship('Producto', back_populates='factura_productos')
