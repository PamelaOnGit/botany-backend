from app import ma 
from models.customer import CustomerModel
from marshmallow import fields


class CustomerSchema(ma.SQLAlchemyAutoSchema): 
    
    orders = fields.Nested('OrderSchema', many=True)

    class Meta:
        model = CustomerModel
        load_instance = True
        include_fk = True

