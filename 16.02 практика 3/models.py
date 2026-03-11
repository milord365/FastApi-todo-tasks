from sqlalchemy import Column, Integer, String, Boolean, Numeric
from database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, default=True)

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)