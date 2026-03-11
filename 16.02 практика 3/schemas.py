from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=80)
    price: float = Field(..., ge=0)
    in_stock: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class StudentBase(BaseModel):
    full_name: str = Field(..., min_length=5, max_length=120)

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)