from app import db 
from models.base import BaseModel

class ImageModel(db.Model, BaseModel):

    __tablename__ = "image_table"

    image_url = db.Column(db.Text, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey('product_table.id'), nullable=False)

    products = db.relationship('ProductModel', back_populates="images")