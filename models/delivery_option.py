from app import db 
from models.base import BaseModel

class DeliveryOptionModel(db.Model, BaseModel): 
    __tablename__ = "delivery_option_table"

    name = db.Column(db.Text, nullable=False, unique=True)

    order = db.relationship("OrderModel", back_populates="delivery_option")


# Relationships
# - order_table - one-(delivery-option)-to-many(-orders)
# - a single order is associated with exactly one delivery option
# - a delivery option can be associated with many orders 

