from fastapi import APIRouter, HTTPException, Query
from typing import List
from .models import Product
from .search import search_products

router = APIRouter()

@router.get("/products/search", response_model=List[Product])
def search(q: str = Query(...), limit: int = 10, skip: int = 0):
    try:
        return search_products(q, limit, skip)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
