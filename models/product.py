from app import db 
from models.base import BaseModel
from models.image import ImageModel
from models.category import CategoryModel
from models.order_line import OrderLineModel


class ProductModel(db.Model, BaseModel): 
    __tablename__ = "product_table"

    name = db.Column(db.Text, nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.id'), nullable=False)
    alt_name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)

    gallery_image = db.relationship('ImageModel', back_populates="product")
    order_lines = db.relationship('OrderLineModel', back_populates="products")
    categories = db.relationship('CategoryModel', back_populates="products", cascade='all, delete')


# Relationships 
# - image_table - one-(product)-to-many-(image)
# a single product can be associated with many images
# every image must be associated with exactly one image