import sqlite3
import logging
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Conexão SQLAlchemy
engine = create_engine(
    f"sqlite:///{settings.ARIA_DB_PATH}",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    """Inicializa o banco de dados do ARIA usando schema.sql caso ele não exista."""
    db_path = Path(settings.ARIA_DB_PATH)
    if not db_path.exists():
        logging.info("Inicializando banco de dados ARIA a partir de schema.sql...")
        schema_path = Path(__file__).parent / "schema.sql"
        if schema_path.exists():
            with sqlite3.connect(db_path) as conn:
                with open(schema_path, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())
            logging.info("Banco de dados ARIA criado com sucesso.")
        else:
            logging.error(f"schema.sql não encontrado no caminho {schema_path}")
    else:
        # Garante que as tabelas de logs existam mesmo se o arquivo DB já existir de execuções parciais
        schema_path = Path(__file__).parent / "schema.sql"
        if schema_path.exists():
            try:
                with sqlite3.connect(db_path) as conn:
                    with open(schema_path, "r", encoding="utf-8") as f:
                        conn.executescript(f.read())
            except Exception as e:
                logging.warning(f"Erro ao re-rodar schema.sql: {e}")

def get_db():
    """Dependency para injeção de sessão nos endpoints do FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
