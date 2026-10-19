# Práctica 1.2: Modelado con Pydantic y Contratos de API

## 1. Justificación Técnica: Schemas de API vs. Modelos de Base de Datos

* **Schema de API (Pydantic):** Representa el **contrato de interfaz/comunicación** entre el cliente y el servidor. Se encarga de la parseación, tipado y validación de los datos JSON que entran (`TaskCreate`) y salen (`TaskRead`) de los endpoints HTTP.
* **Modelo de Base de Datos (ORM / Persistencia):** Representa la **estructura de almacenamiento persistente** en las tablas de la base de datos (por ejemplo, mediante SQLAlchemy).
* **Separación de responsabilidades:** No todos los campos persistidos se reciben del cliente al crear un recurso (ej. `id`, `created_at`, `completed`), ni todos los campos de entrada deben almacenarse directamente. Separar `TaskCreate` y `TaskRead` evita ataques de sobreasignación de atributos (*mass assignment*) y garantiza la integridad de los datos.

---

## 2. Definición de Schemas (`app/schemas.py`)

Se han implementado restricciones mediante `pydantic.Field` en todos los campos relevantes:
* `title`: Mínimo 1 carácter, máximo 100 caracteres.
* `description`: Opcional, máximo 500 caracteres.
* `project_id`: Entero estrictamente positivo (`gt=0`).
* Configuración con `model_config = ConfigDict(from_attributes=True)` para permitir la conversión transparente desde instancias de ORM a dicts/JSON.

---

## 3. Evidencias de Pruebas y Validación (Endpoint `POST /tasks`)

### Caso 1: Petición Válida (Respuesta 201 Created)

**Comando `curl`:**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Diseñar esquema de base de datos",
  "description": "Definir tablas para proyectos y tareas",
  "project_id": 10
}'
