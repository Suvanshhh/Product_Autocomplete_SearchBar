
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
│        ├── products.json
│        ├── main.py
│        ├── search.py
│        ├── routes.py
│        ├── models.py
│   ├── tests/
│        ├── test_search.py
│   ├── venv/
│   ├── requirements.txt
│   └── Dockerfile
│   └── README.md


├── frontend/
│   ├── node_modules
│   └── src/
│        └── components/
│              └── Autocomplete.jsx
│        ├── App.jsx
│        ├── styles.css
│        ├── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── index.html
│   └── Dockerfile
└── docker-compose.yml
└── .gitignore
└── README.md
```

---

# 🧩 BACKEND

### 🎯 Objective
Create a simple backend API that supports product autocomplete functionality. This serves as the backend for a product search feature like an autocomplete box.

> Seeded data source from: [https://dummyjson.com/docs/products](https://dummyjson.com/docs/products)

---

### 🛠 Task Description

#### ✅ 1. Search Products
- Endpoint: `/products/search?q=nescafe&limit=10&skip=0`
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

<h3>🧪 Working using SwaggerUI or Postman:</h3>

Run the project locally (make sure your backend server is running).

Open your browser and navigate to:

http://localhost:8000/docs/


<img src="https://github.com/user-attachments/assets/3fa46723-94d7-4c81-a84d-796c8569c2d0" alt="SwaggerUI Image" width="400"/>


<img src="https://github.com/user-attachments/assets/889aebbf-18e6-43b4-9c0f-9b1b2d81c24a" alt="Postman Image" width="400"/>


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
curl "http://localhost:8000/products/search?q=nescafe&limit=5&skip=0"
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
<img src="https://github.com/user-attachments/assets/c34af5a2-6d51-4eca-ad3f-6b853576ae25" alt="Postman or Swagger Screenshot" width="400"/>


<img src="https://github.com/user-attachments/assets/52b4f521-d693-4610-a741-2c246542981f" alt="Postman Screenshot" width="400"/>



---

# 🎨 FRONTEND

### 🎯 Objective
Build a simple autocomplete component that searches for products using an external API (our FastAPI backend).

---
### Working:
<img src="https://github.com/user-attachments/assets/bfb796f9-cbf4-4076-bd7e-2ba1a29ea087" alt="Swagger UI Running" width="450"/>


<img src="https://github.com/user-attachments/assets/48873e72-86b5-4532-9c7d-a1184928c2a0" alt="Postman Running" width="450"/>


### 🛠 Task Description

#### ✅ 1. Search API
- Fetches suggestions from:
  ```
  http://localhost:8000/products/search?q=nescafe&limit=10&skip=0
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
- ❌ TypeScript not used

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




