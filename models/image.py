from app import db 
from models.base import BaseModel


class ImageModel(db.Model, BaseModel):

    __tablename__ = "image_table"
    
    product_id = db.Column(db.Integer, db.ForeignKey('product_table.id'), nullable=False)

    image_url = db.Column(db.Text, nullable=False)



    product = db.relationship('ProductModel', back_populates="gallery_image")