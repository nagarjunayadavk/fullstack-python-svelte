# 📊 fullstack-python-svelte

The **fullstack-python-svelte** is a full-stack web application using Python with Fast API and Svelte

---

## 🚀 Tech Stack

### 🔧 Backend
- Python (FastAPI)
- SQLAlchemy ORM
- MySQL
- JWT Authentication (basic)

### 🎨 Frontend
- SvelteKit
- Tailwind CSS
- Flowbite-Svelte (UI components)

---

## 📁 Project Structure

fullstack-python-svelte/
├── backend/ # FastAPI backend (app, routes, services, models)
└── frontend/ # SvelteKit frontend (UI + Tailwind)

## ⚙️ Setup Instructions

### ✅ Prerequisites
- Python 3.10+
- Node.js 18+
- MySQL Server 8.0 or 5.7

---

### 1️⃣ Clone the Repository

```
git clone https://github.com/nagarjunayadavk/fullstack-python-svelte.git
cd fullstack-python-svelte
```
### 2️⃣ Backend Setup

cd backend

# Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Linux/Mac
```
# Install dependencies
```
pip install -r requirements.txt
```

# Create and configure .env
cp .env.example .env

# Edit .env with your MySQL DB credentials
go to .env file update corresponding credentials

# Start the FastAPI server

```
uvicorn app.main:app --reload

API runs at: http://localhost:8000
```
### 3️⃣ Frontend Setup (SvelteKit)
```
cd ../frontend
```

# Install dependencies
```
npm install
```

# Start the frontend server
```
npm run dev
UI runs at: http://localhost:5173
```

# DB Setup - install & Create Sample DB with 1 (product) table.
## MySQL Sever & workbench install
https://dev.mysql.com/downloads/installer/

Once installed it will ask to install MySQL Server.

Open again MySQl Community Installer and Go to Catalog, try to Install workbench.

Open workbench and create DBwith new schema.

Follow below steps to crete table and data.

## Product table creation
```
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    quantity INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
#### after starting Backend use below input create API
Send a POST request to:

URL: http://localhost:8000/products

Method: POST

Body (JSON):

```
 #1 -input:
 {
    "name": "Wireless Mouse",
    "description": "2.4GHz optical mouse",
    "price": 799.00,
    "quantity": 25
  }
 #2 - input:
 {
    "name": "Samsung Galaxy S24",
    "description": "6.1-inch Dynamic AMOLED, Exynos 2400, 128GB",
    "price": 79999.00,
    "quantity": 10
  }
#3 - input:
  {
    "name": "iPhone 15 Pro",
    "description": "6.1-inch Super Retina XDR, A17 Pro, 256GB",
    "price": 139900.00,
    "quantity": 5
  }
#4 -input:
  {
    "name": "OnePlus 12R",
    "description": "6.78-inch AMOLED, Snapdragon 8 Gen 2, 256GB",
    "price": 42999.00,
    "quantity": 20
  }
```
Send a GET request to:

URL: http://localhost:8000/products

Method: GET

OutPut:

```
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "description": "2.4GHz optical mouse",
    "price": 799.0,
    "quantity": 25,
    "created_at": "2025-06-25T13:24:19.433Z"
  },
  {
    "id": 2,
    "name": "Samsung Galaxy S24",
    "description": "6.1-inch Dynamic AMOLED, Exynos 2400, 128GB",
    "price": 79999.00,
    "quantity": 10
  },
  {
     "id": 3,
    "name": "iPhone 15 Pro",
    "description": "6.1-inch Super Retina XDR, A17 Pro, 256GB",
    "price": 139900.00,
    "quantity": 5
  },
  {
     "id": 4,
    "name": "OnePlus 12R",
    "description": "6.78-inch AMOLED, Snapdragon 8 Gen 2, 256GB",
    "price": 42999.00,
    "quantity": 20
  }
]
```


🔗 Author

Created by [Nagarjuna Yadav K]
✉️ [nagarjunayadavk@gmail.com]
