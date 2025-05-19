# Design Document

## Endpoints
- `GET /products/search?q=...&limit=...&skip=...`

## Schema
- id, title, brand, category, price

## Pagination
- `limit` and `skip` parameters handle slicing

## Edge Cases
- query < 2 characters => 400
- empty results => 200 with empty list

## Ranking
- Title startswith → +2 score
- Brand startswith → +1 score
