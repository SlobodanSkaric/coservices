from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    status = Column(Integer, nullable=False, default=1)

class Coffes(Base):
    __tablename__ = "coffes"

    coffe_id = Column(Integer, primary_key=True, nullable=False)
    coffe_name = Column(String, nullable=False)
    coffe_addres = Column(String, nullable=False)
    coffe_phone_number = Column(String, nullable=False)
    coffe_email = Column(String, nullable=True)
    coffe_status = Column(Integer, nullable=False, default=1)

class User_Coffe(Base):
    __tablename__ = "user_coffe"

    user_coffe_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    coffe_id = Column(Integer, ForeignKey("coffes.coffe_id", ondelete="CASCADE"), onupdate=False)

    user = relationship("User")
    coffe = relationship("Coffes")