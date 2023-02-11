from app import db 
from models.base import BaseModel 

class BillingAddressModel(db.Model, BaseModel):
    __tablename__ = "billing_address_table"

    customer_id = db.Column(db.Integer, db.ForeignKey('customer_table.id'), nullable=False)
    street_address = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    region = db.Column(db.Text)
    postcode = db.Column(db.Text, nullable=False)

    customer = db.relationship("CustomerModel", back_populates="billing_address")

    # Relationships
    # - customer - many-(billing addresses-)to-many(-customers)
    # a customer can have more than one billing address
    # a billing address can be associated with many customers