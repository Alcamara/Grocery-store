from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: int
    sku: int
    description: str
    price: float

class addProduct(Product):
    id: Optional[int] = None
    pass


class updatePrduct(BaseModel):
    id: Optional[int] = None
    sku: Optional[int] = None
    description: Optional[str] = None
    price: Optional[float] = None