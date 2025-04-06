# Se almacena la plantilla para la documentación de la API
template = {
    "info": {
        "title": "API del Sistema de Facturación y Stock",
        "description": "Documentación generada automáticamente con Swagger",
        "version": "1.0.0"
    },
    "components": {
        "securitySchemes": {
            "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization"
            }
        },
    },
    "security": [
        {
            "ApiKeyAuth": []
        }
    ],
}