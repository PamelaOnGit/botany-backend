from app import db 
from models.base import BaseModel
# !
from models.delivery_address import DeliveryAddressModel
from models.delivery_option import DeliveryOptionModel
from models.order_status import OrderStatusModel




class OrderModel(db.Model, BaseModel): 
    __tablename__ = "order_table"

    customer_id = db.Column(db.Integer, db.ForeignKey('customer_table.id'), nullable=False)
    delivery_address_id = db.Column(db.Integer, db.ForeignKey('delivery_address_table.id'), nullable=False)
    delivery_option_id = db.Column(db.Integer, db.ForeignKey('delivery_option_table.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False, default=0.0)
    # possibly require a default order status here eg.0 
    order_status_id = db.Column(db.Integer, db.ForeignKey('order_status_table.id'), default=0, nullable=False)

    customers = db.relationship("CustomerModel", back_populates="order", cascade='all, delete')
    delivery_address = db.relationship("DeliveryAddressModel", back_populates="order", cascade='all, delete')
    delivery_option = db.relationship("DeliveryOptionModel", back_populates="order", cascade='all, delete')
    order_status = db.relationship("OrderStatusModel", back_populates="order", cascade='all, delete')

    # order_lines = db.relationship("OrderLineModel", back_populates='orders')




# Relationships 

# - customer_table - many-(orders)-to-one(-customer) 
# a single customer can be associcated with many order
# a single order must be associated with exactly one customer

# - delivery_address_table -many(orders)-to-one(-delivery-address)
# a single order is associated with exactly one delivery address
# a delivery address can be associated with many order

# -delivery_option_table -many-(orders-)to-one(-delivery-option)
# a single order is associated with exacltly one delivery option
# a delivery option is associated with many orders

# -order_status_table -many-(orders-)to-one(-order-status)
# a singe order is associated with exaclty one orderstatus at a time
# an order status is associated with many orders

