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
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Create and configure .env
cp .env.example .env

# Edit .env with your MySQL DB credentials

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

🔗 Author

Created by [Nagarjuna Yadav K]
✉️ [nagarjunayadavk@gmail.com]
