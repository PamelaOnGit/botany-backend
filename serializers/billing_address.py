from app import ma
from models.billing_address import BillingAddressModel

class BillingAddressSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = BillingAddressModel
        load_instance = True
        # include_fk = True

