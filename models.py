from databases import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime


class BillBoard(Base):
    
    __tablename__ = 'billboards'
    id = Column(Integer, primary_key=True, index=True, nullable = False)
    location = Column(String)
    width = Column(Integer, default=None)
    height = Column(Integer, default=None)
    code = Column(String, default=None)
    rent = Column(String, default=None)
    is_available = Column(Boolean)
    reserved_at = Column(String, default=None)
    reserved_until = Column(String, default=None)
    created_at = Column(DateTime, default=datetime.utcnow())
    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("Owner", back_populates='billboards')
    

class Owner(Base):
    
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, index=True, nullable = False)
    name = Column(String)
    phone_number = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    billboards = relationship("BillBoard", back_populates='owner')


class User(Base):
    
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, nullable = False)
    phone_number = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    