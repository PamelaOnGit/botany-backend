from app import db 
from models.base import BaseModel
from models.order import OrderModel
# !
from models.customer_billing_address import CustomerBillingAddressModel



class CustomerModel(db.Model, BaseModel): 
    __tablename__ = "customer_table"

    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)

    order = db.relationship("OrderModel", back_populates="customers")
    
    customer_billing_addresses = db.relationship("CustomerBillingAddressModel", back_populates="customers")


# Relationships 
#  - billing_address_table - many-to-many
# a customer can have more than one billing address
# a billing address can be associated with more than one customer


# - order_table - one-to-many
# a customer can make many orders
# an order is associated with exactly one customer

