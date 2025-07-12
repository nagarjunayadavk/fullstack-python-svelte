from fastapi import FastAPI
from app.database import engine
from app.models import Base  # imported from __init__.py
from app.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Backend is running!"} 

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(api_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)