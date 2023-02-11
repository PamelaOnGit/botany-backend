from app import db 
from models.base import BaseModel

class OrderStatusModel(db.Model, BaseModel): 

    __tablename__= "order_status_table"

    name = db.Column(db.Text, nullable=False, unique=True)

    order = db.relationship("OrderModel", back_populates="order_status")


# Relationships one(-order-status)-to-many(-orders)

# - order_table 
# every order must have exactly one order_status
# an order status can be associated with many orders


