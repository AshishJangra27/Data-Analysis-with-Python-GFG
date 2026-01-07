from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint 
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(' sqlite:///example.db')
Base = declarative_base()

class User (Base) :
  _tablename_ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column (String, nullable=False)
  email = Column(String, unique=True, nullable=False)
  _table_args_ = (UniqueConstraint(' email'),)
  
Session = sessionmaker (bind=engine)
session = Session()

users = [
      User (name="Carol", email="carol@example.com"), User (name="Dave", email="dave@example.com"), User (name="Eve", email="eve@example. com")
]
session.add_alllusers)
session.commit()
