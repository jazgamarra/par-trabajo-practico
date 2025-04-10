from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.cliente import Cliente

from app import db

class Factura(db.Model):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    numero = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    cliente = relationship('Cliente', backref='facturas')
    factura_productos = db.relationship('FacturaProducto', back_populates='factura', cascade='all, delete-orphan')
