from app.search import search_products

def test_basic_search():
    results = search_products("iphone")
    assert isinstance(results, list)
    assert len(results) > 0
