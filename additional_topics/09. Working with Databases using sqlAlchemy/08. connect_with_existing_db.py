from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus

# -----------------------------
# Database credentials
# -----------------------------
HOST = 'localhost'        # fixed typo
USER = 'root'
PASSWORD = 'gfg@1998'     # fixed string
DATABASE = 'myntra'

# Encode password (important for special characters)
PASSWORD_ENCODED = quote_plus(PASSWORD)

# -----------------------------
# Database connection
# -----------------------------
engine = create_engine(
    f"mysql+mysqlconnector://{USER}:{PASSWORD_ENCODED}@{HOST}/{DATABASE}",
    echo=True
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------
# Model definition
# -----------------------------
class User(Base):
    __tablename__ = 'user'   # fixed __tablename__

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    __table_args__ = (
        UniqueConstraint('email', name='uq_user_email'),
    )

# -----------------------------
# Create tables
# -----------------------------
Base.metadata.create_all(engine)

# -----------------------------
# Insert a user
# -----------------------------
new_user = User(
    name="Alice",
    email="alice@example.com"
)

session.add(new_user)
session.commit()

# -----------------------------
# Query users
# -----------------------------
users = session.query(User).all()
print("All users:")
for u in users:
    print(u.id, u.name, u.email)

# -----------------------------
# Update a user
# -----------------------------
alice = session.query(User).filter_by(name="Alice").first()
if alice:
    alice.email = "alice@newdomain.com"
    session.commit()

# -----------------------------
# Delete a user
# -----------------------------
alice = session.query(User).filter_by(name="Alice").first()
if alice:
    session.delete(alice)
    session.commit()

# -----------------------------
# Close session
# -----------------------------
session.close()
