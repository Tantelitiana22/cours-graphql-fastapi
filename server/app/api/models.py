from typing import Optional
import uuid
from pydantic import BaseModel


class ProductModel(BaseModel):
    id_type: str
    name: str
    category: str
    filter: str
    price: float


class ProductModelShow(BaseModel):
    _id: str
    id_type: str
    name: str
    category: str
    filter: str
    price: float


class ProductModelOptional(BaseModel):
    id_type: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    filter: Optional[str] = None
    price: Optional[float] = None
