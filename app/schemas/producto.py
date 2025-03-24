# app/schemas/producto.py
from app import ma
from app.models.producto import Producto

class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =  Producto # definimos que este esquema es para producto
        load_instance = True # permite convertir json a objetos de la clase producto
