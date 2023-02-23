from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get('/')
# def get_product():
#     return {"fruit":"Apple"}

@app.get('/products')
def get_products(skip:int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_all_products(db,skip=skip, limit=limit)
    return products

@app.post('/product/')
def add_product(product:schemas.addProduct, db: Session = Depends(get_db)):
    return crud.add_products(db=db, product=product)

@app.put('/product/{product_id}')
def update_product(product_id: int, product: schemas.updatePrduct , db: Session = Depends(get_db)):
    update_product = crud.update_product(int(product_id), new_product_update=product, db=db)
    return update_product

@app.delete('/remove-product/{product_id}')
def delete_product(product_id:int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(id=product_id, db=db)
    return product_id