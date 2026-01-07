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

bob = session.query(User).filter_by(name="Bob").first()
if bob:
  bob.email = "bob@newdomain.com"
  bob.name = "Boby"
  session.commit()
  print('User updated successfully. ')
else:
  print('User not found. ')
  
session.close()
