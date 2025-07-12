from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(product: dict, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return product_service.get_all_products(db)

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product_by_id(db, product_id)

@router.put("/{product_id}")
def update_product(product_id: int, updates: dict, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, updates)

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)
