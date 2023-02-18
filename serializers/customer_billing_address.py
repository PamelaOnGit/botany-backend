from app import ma 
from models.customer_billing_address import CustomerBillingAddressModel

class CustomerBillingAddressSchema(ma.SQLAlchemyAutoSchema): 
    class Meta: 
        model = CustomerBillingAddressModel
        load_instance = True
        # include_fk = True