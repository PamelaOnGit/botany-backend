from app import db 
from models.base import BaseModel
from models.order import OrderModel

class DeliveryAddressModel(db.Model, BaseModel): 
    __tablename__ = "delivery_address_table"

    name = db.Column(db.Text, nullable=False)
    street_address = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    region = db.Column(db.Text)
    postcode = db.Column(db.Text, nullable=False)

    order = db.relationship("OrderModel", back_populates="delivery_address")

    # orders = db.relationship('OrderModel', backref='order_table', cascade='all, delete')
    # Relationships

    # - order-table - one-to-many
    # a delivery address can recieve many orders
    # each order is associated with exactly one delivery address

  