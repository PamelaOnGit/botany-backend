from app import ma 
from models.delivery_address import DeliveryAddressModel

class DeliveryAddressSchema(ma.SQLAlchemyAutoSchema):

    class Meta: 
        model = DeliveryAddressModel
        load_instance = True
        # include_fk = True

   
