from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexión a la base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskflow.db"

# Engine con check_same_thread=False para evitar problemas de hilos en SQLite con FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

Base = declarative_base()


# Dependencia get_db() con ciclo de vida garantizado mediante try/finally y yield
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
