# Práctica 1.4: Middlewares y Manejo Global de Excepciones

## 1. Concepto y Justificación de Middlewares

Un **middleware** es un componente de software que se sitúa entre la llegada de la petición HTTP del cliente y la ejecución final del endpoint en FastAPI. Permite añadir comportamiento transversal (*cross-cutting concerns*) como la gestión de CORS, auditoría de métricas, inyección de identificadores de trazabilidad o autenticación.

### Middlewares Implementados
1. **`CORSMiddleware`**: Restringe el acceso entre dominios (*Cross-Origin Resource Sharing*). Permite solicitudes exclusivamente desde orígenes autorizados como `http://localhost:5173` (Frontend en Vite/React) previniendo ataques maliciosos desde otros dominios. Expone de manera explícita las cabeceras personalizadas mediante `expose_headers`.
2. **Middleware `X-Process-Time` y `X-Request-ID`**:
   - Mide el tiempo de ejecución de la petición en milisegundos (`perf_counter()`).
   - Inyecta un UUID único `X-Request-ID` que permite la trazabilidad completa de cada petición a lo largo de los logs del sistema.

---

## 2. Seguridad en el Manejo Global de Excepciones

El manejador global de excepciones `@app.exception_handler(Exception)` intercepta cualquier error no capturado (ej. división por cero, fallos de base de datos):

* **Prevención de fuga de información (*Information Disclosure*):** Nunca se expone el *stacktrace* de Python ni detalles internos del servidor en la respuesta HTTP al cliente final.
* **Logging Interno:** El error técnico completo junto con el *traceback* se registra exclusivamente en los logs del servidor (`logger.error(..., exc_info=True)`).
* **Respuesta Homogénea (HTTP 500):** Devuelve un esquema estructurado estandarizado con un código `INTERNAL_SERVER_ERROR`.

---

## 3. Orden de Ejecución de Middlewares

Los middlewares en FastAPI/Starlette envuelven la aplicación en forma de capas (cebolla):
1. **Petición entrante:** `CORS` $\rightarrow$ `Métricas/Process-Time` $\rightarrow$ `Router/Endpoint`.
2. **Respuesta saliente:** `Router/Endpoint` $\rightarrow$ `Métricas/Process-Time` (añade cabeceras) $\rightarrow$ `CORS` (valida cabeceras de origen) $\rightarrow$ Cliente.

Por ello, el registrador de tiempo y logging debe ejecutarse en la capa más externa posible respecto a la lógica de negocio para capturar la duración real total y capturar cualquier excepción.
