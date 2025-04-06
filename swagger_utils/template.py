# OpenAPI template for the Swagger documentation.
template = {
    "info": {
        "title": "API de Sistema de Facturación y Stock",
        "description": "API para gestionar facturas, productos, clientes, proveedores, etc.",
        "version": "1.0.0"
    },
    "components": {
        "schemas": {
            "Producto": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "nombre": {"type": "string"},
                    "precio": {"type": "number"},
                    "descripcion": {"type": "string"}
                },
                "required": ["nombre", "precio"]
            }
        }
    }
}
