from sqlalchemy.orm import Session

import models, schemas

def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).order_by(models.Product.id).offset(skip).limit(limit).all()

def add_products(db: Session, product: schemas.addProduct):
    new_product = models.Product(
        sku=product.sku, 
        description=product.description, 
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update_product(id: int, new_product_update: schemas.updatePrduct ,db: Session):

    product_to_update = db.query(models.Product).get(id)

    if new_product_update.sku != None:
        product_to_update.sku = new_product_update.sku 

    if new_product_update.description != None:
        product_to_update.description =new_product_update.description 

    if new_product_update.price != None:
        product_to_update.price = new_product_update.price

    db.commit()
    db.refresh(product_to_update)

    return product_to_update


def delete_product(id:int, db:Session):
    product_to_delete = db.query(models.Product).get(id)
    db.delete(product_to_delete)
    db.commit()
    db.refresh(product_to_delete)
    return "done"
