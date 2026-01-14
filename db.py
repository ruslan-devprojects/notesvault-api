import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DEFAULT_DB_URL = "sqlite:///./notesvault.db"

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB_URL)

# Clean up common copy/paste issues from dashboards
DATABASE_URL = DATABASE_URL.strip().strip('"').strip("'")

# Normalize scheme for SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# If using psycopg v3 explicitly, this also works:
# postgresql+psycopg://user:pass@host/dbname
# (postgresql://... is fine too)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass
