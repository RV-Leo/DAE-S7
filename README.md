# DAE-S7: ORM en Django — Laboratorio S07

## Desarrollo de Aplicaciones Empresariales — 4-C24-A

### Paso 1 — Estructura del proyecto

- Proyecto Django `config/` con `manage.py`.
- App `blog` declarada en `INSTALLED_APPS`.
- Pillow instalado en `requirements.txt`.
- Plantillas configuradas con `DIRS` apuntando a cada `templates/` de las apps.
- Archivos estáticos configurados (`STATIC_URL = "static/"`).

### Paso 2 — Modelos y migraciones

Modelos declarados en `blog/models.py`:

| Modelo      | Campo clave                                  | Relación        |
|-------------|-----------------------------------------------|-----------------|
| Author      | `name`                                        | —               |
| Profile     | `author` (OneToOne), `country`, `bio`         | Uno a uno       |
| Category    | `name` (unique)                               | —               |
| Tag         | `name` (unique)                               | —               |
| Post        | `title`, `body`, `published`, `published_at`  | ForeignKey a Author y Category; ManyToMany a Tag |
| Comment     | `author_name`, `text`, `created_at`           | ForeignKey a Post |

Migración `0001_initial.py` generada y aplicada correctamente.
Seed cargado: 4 autores, 15 artículos, 23 comentarios.
