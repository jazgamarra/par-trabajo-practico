# Trabajo practico 1 de la asignatura Prog. de Aplicaciones en redes - API REST 

## Para ejecutar el proyecto 
**Crear y activar un entorno virtual**

En windows, la creacion se realiza con el comando `python -m venv venv`.
Para activarlo, ingresar a la carpeta `venv\Scripts` y ejecutar el comando `activate`

**Instalar los requerimientos**

Para este paso se necesita tener pip para manejar los paquetes.
Los requerimientos se instalan una vez activado el entorno virtual, con el comando `pip install -r requirements.txt`

**Conectar la base de datos**
- Es necesario tener una base de datos PostgreSQL creada para el siguiente paso. 
- Crear un archivo .env con los parametros de conexion a la base de datos \
  `DATABASE_URL=postgresql://[usuario]:[password]@localhost:[puerto]/[nombre_de_la_bd]` \
  Ejemplo: `DATABASE_URL=postgresql://postgres:postgres@localhost:5432/trabajopractico_db`
- Realizar las migraciones con los siguientes comandos: 
  `flask db init` \
  `flask db migrate` \
  `flask db update` 

**Levantar el servidor**

Ejecutar archivo `run.py`

## Acceder a la documentacion 
Ejecutar el proyecto para correr el servidor e ingresar a la url `http://localhost:5000/apidocs`

## URL base para pruebas 
`http://localhost:5000`
