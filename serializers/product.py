from app import ma 
from models.product import ProductModel
from marshmallow import fields

class ProductSchema(ma.SQLAlchemyAutoSchema):

    gallery_image = fields.Nested('ImageSchema', many=True)
    
    class Meta: 

        model = ProductModel       
        load_instance = True
        include_fk = True