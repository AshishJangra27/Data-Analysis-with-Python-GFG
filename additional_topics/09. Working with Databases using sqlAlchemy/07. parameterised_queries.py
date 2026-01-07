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

user_name = input('Enter name to search: ')
result = session.query(User).filter_by(name=user_name).all()
print('Search result:', [(u.id, u.name, u.email) for u in result])

session.close()
