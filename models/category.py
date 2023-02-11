from app import db 
from models.base import BaseModel

class CategoryModel(db.Model, BaseModel): 
    __tablename__ = 'category_table'
     
    name = db.Column(db.Text, nullable=False, unique=True)


    products = db.relationship('ProductModel', backref='product_table', cascade='all, delete')

  # Relationships 
  # product_table - one-(category-)to-many(-product)
# a product must have exactly one category
# a category can be associated with many products

