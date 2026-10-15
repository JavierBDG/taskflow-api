# Práctica 1.3: Despliegue de TaskFlow API con Gunicorn y UvicornWorker

## 1. Comandos de Instalación y Ejecución

```bash
# Activación del entorno e instalación de dependencias
source ~/venv-linux/bin/activate
pip install fastapi uvicorn gunicorn pydantic

# Ejecución del servidor de aplicaciones
gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000
<img width="817" height="472" alt="Captura de pantalla 2026-10-15 224410" src="https://github.com/user-attachments/assets/d40623d3-f424-4000-9720-1092d1cb8ec5" />

curl -i [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
# HTTP/1.1 200 OK -> {"status":"ok"}

curl -i [http://127.0.0.1:8000/version](http://127.0.0.1:8000/version)
# HTTP/1.1 200 OK -> {"version":"1.0.0","app_name":"TaskFlow API"}

curl -i [http://127.0.0.1:8000/ping](http://127.0.0.1:8000/ping)
# HTTP/1.1 200 OK -> {"message":"pong"}

Justificación Técnica y Teórica
WSGI vs ASGI
WSGI (Web Server Gateway Interface): Estándar síncrono tradicional para Python (Django, Flask). Procesa una petición por hilo/proceso bloqueante.

ASGI (Asynchronous Server Gateway Interface): Estándar asíncrono moderno que permite gestionar miles de conexiones concurrentes mediante async/await, WebSockets y HTTP/2. FastAPI está construido sobre ASGI.

Rol de Gunicorn y UvicornWorker
Gunicorn: Actúa como Process Manager (Master Process). Gestiona la vida de los trabajadores, reinicia procesos caídos y escala horizontalmente según los núcleos de la CPU.

UvicornWorker: Es la clase de trabajador que permite a Gunicorn ejecutar el bucle de eventos asíncrono (uvicorn.workers.UvicornWorker) para procesar las peticiones ASGI de FastAPI.

Direcciones de Binding (127.0.0.1 vs 0.0.0.0)
127.0.0.1 (Loopback): Solo acepta tráfico local desde la propia máquina (ideal tras un proxy inverso como Nginx).

0.0.0.0: Escucha en todas las interfaces de red disponibles, exponiendo el servicio a la red externa.

Operación y Depuración
Detener procesos colgados en puerto 8000:

Bash
pkill -f gunicorn
sudo fuser -k 8000/tcp
