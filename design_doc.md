
# 🧩 Design Document — Product Autocomplete Backend (FastAPI)

---

## ✅ API Structure & Endpoint

### `/products/search`
**Method**: GET  
**Description**: Returns a list of products that match a query string based on `title` or `brand`.

**Query Parameters**:
- `q` (string, required): search term (minimum 2 characters)
- `limit` (int, optional): number of results per page (default = 10)
- `skip` (int, optional): offset for pagination (default = 0)

**Example**:
```
/products/search?q=iphone&limit=5&skip=0
```

---

## 🧱 Data Schema

Each product is a JSON object with the following structure:

```json
{
  "id": 1,
  "title": "iPhone 9",
  "brand": "Apple",
  "category": "smartphones",
  "price": 549
}
```

Data is stored locally in `products.json`, seeded from [dummyjson.com/products](https://dummyjson.com/products). Total entries: 100+

---

## 📊 Pagination Logic & Edge Case Handling

Pagination is handled using:
- `limit`: determines how many results to return
- `skip`: determines how many results to skip (offset)

**Edge Cases**:
- If `q` is missing or < 2 characters → returns 400 error with a validation message.
- If no matches found → returns empty list with `200 OK`.
- If `limit` or `skip` are non-integer → returns 422 validation error.

---

## ⚙️ Assumptions & Limitations

### Assumptions:
- Products are static and loaded in-memory from a JSON file.
- `title` and `brand` are both always present in each product.
- All input is expected as query parameters.

### Limitations:
- No fuzzy matching (e.g., typo tolerance)
- Not scalable for large datasets (due to in-memory search)
- No persistent database

---

## 🧠 Bonus: Scoring & Ranking Logic

To improve result relevance:
- Products where the `title` **starts with** the query are ranked highest (+2 points)
- If `brand` starts with query → (+1 point)
- Other matches that contain query → (0 points)

Final result list is sorted based on the total score in descending order before pagination is applied.

---

## ✅ Summary

This FastAPI-based backend is optimized for performance, clarity, and correctness for an autocomplete-style product search. It handles validation, edge cases, ranking, and pagination with clean modular code.
