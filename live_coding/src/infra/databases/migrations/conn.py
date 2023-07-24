from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = 'postgresql://user:@localhost:5455/postgres'
Base = declarative_base()

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(bind=engine)
session_orm = Session(bind=engine)

Base.metadata.create_all(bind=engine)