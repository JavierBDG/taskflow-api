# Práctica 1.5: Modelos SQLAlchemy y Conexión a Base de Datos

## 1. Concepto de ORM y Ventajas Frente a SQL Directo

Un **ORM (Object-Relational Mapping)** como **SQLAlchemy** mapea las tablas relacionales de la base de datos a clases de Python, permitiendo interactuar con los datos mediante objetos y métodos sin necesidad de escribir sentencias SQL manuales.

### Comparativa: ORM vs. SQL Directo
* **Ventajas del ORM:**
  - **Portabilidad:** Se puede cambiar de motor de BD cambiando únicamente la cadena de conexión (`engine`).
  - **Seguridad:** Previene ataques de inyección SQL mediante la parametrización automática de consultas.
  - **Mantenibilidad:** Mantiene la lógica del modelo de datos sincronizada con las clases del lenguaje.
* **Cuándo usar SQL directo:** En consultas complejas analíticas, reportes masivos o cuando se requiera exprimir al máximo el rendimiento mediante optimizaciones nativas específicas del motor de BD.

---

## 2. Configuración del Engine y Ciclo de Vida de la Sesión

### Engine (`database.py`)
* `check_same_thread=False`: Permite que múltiples hilos de solicitudes asincrónicas en FastAPI compartan la conexión de SQLite.
* `pool_pre_ping=True`: Verifica la validez de las conexiones en el pool antes de entregarlas para evitar errores de conexión muerta.

### Inyección de Dependencias `get_db()`
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
