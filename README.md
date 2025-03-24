# par-trabajo-practico
Trabajos practicos de la asignatura Prog. de Aplicaciones en redes 

## Para hacer pruebas 
curl http://127.0.0.1:5000/productos/1
curl -X POST http://127.0.0.1:5000/productos -H "Content-Type: application/json" -d "{\"nombre\": \"Teclado mecánico\", \"precio\": 150, \"descripcion\": \"RGB\"}"

## Comandos relacionados a la bd 
db init     → Prepara el sistema de migraciones.
db migrate  → Detecta cambios en modelos y los convierte a instrucciones.
db upgrade  → Aplica esas instrucciones a la base de datos real.
