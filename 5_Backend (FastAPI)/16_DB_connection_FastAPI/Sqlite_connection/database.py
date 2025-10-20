# The database to be connected/create defined here

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# defining the SQLite Db file path
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# creating the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# creating session class
sessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind = engine
)

# base class for tables(models)
Base = declarative_base()