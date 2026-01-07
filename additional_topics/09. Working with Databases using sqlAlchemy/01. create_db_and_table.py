from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')
Base = declarative_base()

class User (Base) :
  _tablename_ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False)
  _table_args_ = (UniqueConstraint(' email'),)

Base.metadata.create_all(engine)
print('Table created successfully. ')
