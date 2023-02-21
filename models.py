from sqlalchemy import Boolean, Column, Integer, String, Float

from database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(Integer)
    description = Column(String)
    price = Column(Float)