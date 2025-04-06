# API REST 
Trabajos practicos de la asignatura Prog. de Aplicaciones en redes 

## Para ejecutar el proyecto 
**Crear y activar un entorno virtual**

En windows, la creacion se realiza con el comando `python -m venv venv`.
Para activarlo, ingresar a la carpeta `venv\Scripts` y ejecutar el comando `activate`

**Instalar los requerimientos**

Para este paso se necesita tener pip para manejar los paquetes.
Los requerimientos se instalan una vez activado el entorno virtual, con el comando `pip install -r requirements.txt`

## Acceder a la documentacion 
Ejecutar el proyecto para correr el servidor e ingresar a la url `http://localhost:5000/apidocs`

## Para hacer pruebas 
curl http://127.0.0.1:5000/productos/1
curl -X POST http://127.0.0.1:5000/productos -H "Content-Type: application/json" -d "{\"nombre\": \"Teclado mecánico\", \"precio\": 150, \"descripcion\": \"RGB\"}"

## Comandos relacionados a la bd 
db init     → Prepara el sistema de migraciones.
db migrate  → Detecta cambios en modelos y los convierte a instrucciones.
db upgrade  → Aplica esas instrucciones a la base de datos real.

