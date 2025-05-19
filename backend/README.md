# Product Autocomplete API

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Sample Request
```bash
curl "http://127.0.0.1:8000/products/search?q=iphone&limit=5&skip=0"
```
