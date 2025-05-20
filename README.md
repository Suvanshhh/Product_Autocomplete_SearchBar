
# 🔍 Product Autocomplete — Full Stack Application

This project implements a **full-stack product autocomplete application** consisting of:
- A **FastAPI backend** that provides a product search API
- A **React frontend** that consumes the API and displays suggestions in an autocomplete dropdown

---

## 📁 Project Structure

```
Search_autocomplete/
├── backend/
│   ├── app/
│   ├── products.json
│   ├── main.py
│   ├── search.py
│   ├── routes.py
│   ├── models.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── public/
│   ├── App.jsx
│   ├── components/
│   ├── styles.css
│   ├── package.json
│   └── Dockerfile
└── docker-compose.yml
```

---

# 🧩 BACKEND

### 🎯 Objective
Create a simple backend API that supports product autocomplete functionality. This serves as the backend for a product search feature like an autocomplete box.

> Seeded data source from: [https://dummyjson.com/docs/products](https://dummyjson.com/docs/products)

---

### 🛠 Task Description

#### ✅ 1. Search Products
- Endpoint: `/products/search?q=phone&limit=10&skip=0`
- Returns a list of products where `title` or `brand` **contains the query string** (case-insensitive)
- Results are **paginated** using `limit` and `skip`

#### ✅ 2. Minimum Query Length
- If `q` is shorter than 2 characters → `400 Bad Request`

#### ✅ 3. Simulate Data Source
- Uses a static file-based JSON (`products.json`)
- Includes at least 100 entries with:
  - `id`
  - `title`
  - `brand`
  - `category`
  - `price`

#### ✅ 4. Performance Optimization (Simulated)
- In-memory search
- Scoring logic:
  - Matches where **title starts with** query get higher priority
  - Matches in brand are ranked slightly lower

#### ✅ 5. Error Handling & Validation
- Returns meaningful HTTP status codes and messages
- Validates required query parameters

---

### 🧠 Bonus Points Addressed

- ✅ Clean, modular structure (`search.py`, `routes.py`, `models.py`)
- ✅ FastAPI + Pydantic
- ✅ CORS enabled
- ✅ Can be started with:
  ```bash
  uvicorn app.main:app --reload
  ```
- ✅ Dockerfile included for backend

---

### 🧪 Sample API Test (curl)

```bash
curl "http://localhost:8000/products/search?q=apple&limit=5&skip=0"
```

---

### 🧭 Backend Setup

#### Using Python:
```bash
cd backend
python -m venv venv
.env\Scriptsctivate     # or source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Using Docker:
```bash
docker-compose up --build
```

---

# 🎨 FRONTEND

### 🎯 Objective
Build a simple autocomplete component that searches for products using an external API (our FastAPI backend or DummyJSON as fallback).

---

### 🛠 Task Description

#### ✅ 1. Search API
- Fetches suggestions from:
  ```
  http://localhost:8000/products/search?q=phone&limit=10&skip=0
  ```

#### ✅ 2. Pagination Support
- Uses `limit` and `skip` parameters

#### ✅ 3. Optimizations
- API call only triggers after typing **2 or more characters**
- Debounced to avoid firing on every keystroke

#### ✅ 4. Dropdown UI
- Shows matching product suggestions with `title` and `brand`

#### ✅ 5. Loading Indicator
- Spinner or loading text shown during API fetch

---

### 🧠 Bonus Points Addressed

- ✅ React Hooks used (`useState`, `useEffect`, `useRef`)
- ✅ Modular structure (`Autocomplete.jsx`)
- ✅ CSS-based clean and minimal UI
- ✅ Error handling if API fails or returns no results
- ❌ TypeScript not used (as per spec request)

---

### 🧭 Frontend Setup

#### Using Node:
```bash
cd frontend
npm install
npm run dev
```

#### Using Docker:
```bash
docker-compose up --build
```

> Accessible at: [http://localhost:5173](http://localhost:5173)

---

## 🧠 Thought Process / Approach

- Broke the backend into clean, testable modules (routing, logic, models)
- Downloaded and structured product data for real-world relevance
- Implemented frontend autocomplete with debouncing, minimum query, and graceful loading/error UX
- Dockerized both apps for single-command deployment and easier review
- Designed with clean file structure and modularity in mind

---

## 🔗 Final GitHub Repository Link

> [https://github.com/your-username/search-autocomplete-fullstack](https://github.com/your-username/search-autocomplete-fullstack)

---

✅ Both **Frontend** and **Backend** are compliant with their assignment specifications and ready for deployment or evaluation.
