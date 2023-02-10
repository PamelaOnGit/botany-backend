from app import db 
from models.base import BaseModel
from models.image import ImageModel


class ProductModel(db.Model, BaseModel): 
    __tablename__ = "products_table"

    name = db.Column(db.Text, nullable=False, unique=True)
    category = db.Column(db.Text, nullable=False)
    alt_name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)

    images = db.relationship('ImageModel', backref='images_table', cascade='all, delete')

