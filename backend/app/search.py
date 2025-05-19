import json
from typing import List
from .models import Product

with open("app/products.json") as f:
    product_data = json.load(f)["products"]

PRODUCTS = []

for item in product_data:
    try:
        product = Product(
            id=item.get("id"),
            title=item.get("title", ""),
            brand=item.get("brand", ""),          # default empty string
            category=item.get("category", ""),
            price=item.get("price", 0.0)
        )
        PRODUCTS.append(product)
    except Exception as e:
        print(f"Skipping invalid product: {e}")


def search_products(q: str, limit: int = 10, skip: int = 0) -> List[Product]:
    if len(q) < 2:
        raise ValueError("Query must be at least 2 characters long.")

    results = []
    q_lower = q.lower()

    for product in PRODUCTS:
        title_match = product.title.lower().find(q_lower)
        brand_match = product.brand.lower().find(q_lower)
        if title_match != -1 or brand_match != -1:
            score = 0
            if product.title.lower().startswith(q_lower):
                score += 2
            if product.brand.lower().startswith(q_lower):
                score += 1
            results.append((score, product))

    sorted_results = sorted(results, key=lambda x: -x[0])
    return [p for _, p in sorted_results][skip:skip + limit]
