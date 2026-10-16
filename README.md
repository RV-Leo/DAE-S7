# ORM con IA duelo y verificador

## Contexto

Laboratorio DAE S07 Extra de Desarrollo de Aplicaciones Empresariales. El proyecto compara consultas ORM escritas por el estudiante con respuestas de IA, verifica resultados y coste mediante un duelo automático, y demuestra límites seguros para las acciones que una aplicación puede ejecutar a partir de una intención.

## Tecnologías usadas

- Python 3.11.9 en el entorno de este equipo (el laboratorio recomienda Python 3.12 o superior).
- Django 5.2.18.
- SQLite para desarrollo y pruebas.
- Git y GitHub.

## Estructura del proyecto

- `config/`: configuración y rutas del proyecto Django.
- `blog/models.py`: modelos de autores, perfiles, categorías, artículos, etiquetas y comentarios.
- `blog/duel/`: preguntas, respuestas de referencia de IA, respuestas del equipo y verificador.
- `blog/agent/`: adaptador del modelo y registro cerrado de acciones.
- `blog/queries.py`: consulta optimizada para la portada.
- `blog/management/commands/`: comandos `seed_blog`, `duel` y `agent`.
- `blog/tests/`: pruebas de datos, consultas, duelo y frontera de seguridad.
