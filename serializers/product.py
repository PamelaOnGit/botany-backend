from app import ma 
from models.product import ProductModel
from marshmallow import fields

class ProductSchema(ma.SQLAlchemyAutoSchema): 
    
    # fields enables all the images to be included inside 
    # the product object when the product is deseialized

    images = fields.Nested('ImageSchema', many=True)
    
    class Meta: 

        model = ProductModel       
        load_instance = True