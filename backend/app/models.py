from pydantic import BaseModel

class Product(BaseModel):
    id: int
    title: str
    brand: str
    category: str
    price: float
