from app import db 
from models.base import BaseModel

class ImageModel(db.Model, BaseModel):

    __tablename__ = "images_table"

    image_url = db.Column(db.Text, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey('products_table.id'), nullable=False)