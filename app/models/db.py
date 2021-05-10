from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/home_inspector.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
