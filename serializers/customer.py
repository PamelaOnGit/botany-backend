from app import ma 
from models.customer import CustomerModel
from marshmallow import fields


class CustomerSchema(ma.SQLAlchemyAutoSchema): 
    
    billing_address = fields.Nested('BillingAddressSchema', many=True)
  
    class Meta:
        model = CustomerModel
        load_instance = True
        # include_fk = True

