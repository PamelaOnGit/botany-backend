from app import db
from models.base import BaseModel
# !
from models.billing_address import BillingAddressModel




class CustomerBillingAddressModel(db.Model, BaseModel): 
    __tablename__ = "customer_billing_address_table"

    customer_id = db.Column(db.Integer, db.ForeignKey('customer_table.id'))
    billing_address_id = db.Column(db.Integer, db.ForeignKey('billing_address_table.id'))

    customers = db.relationship('CustomerModel', back_populates="customer_billing_addresses", cascade='all, delete')
    billing_addresses = db.relationship('BillingAddressModel', back_populates='customers', cascade='all, delete')