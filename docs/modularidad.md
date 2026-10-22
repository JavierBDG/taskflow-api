# Práctica 1.3: Organización Modular con APIRouter

## 1. Justificación de la Estructura Modular

A medida que una API crece, mantener todas las definiciones de endpoints en un único archivo (`main.py`) genera un código monolítico, difícil de mantener y propenso a conflictos en equipos de desarrollo.

### Estructura del Proyecto

```text
taskflow-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       ├── projects.py
│       └── tasks.py
├── docs/
│   ├── arquitectura.md
│   ├── gunicorn.md
│   ├── modularidad.md
│   └── pydantic.md
├── Dockerfile
└── requirements.txt
