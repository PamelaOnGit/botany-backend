from app import ma 
from models.order_status import OrderStatusModel
from marshmallow import fields

class OrderStatusSchema(ma.SQLAlchemyAutoSchema):

    class Meta: 
        model = OrderStatusModel
        load_instance = True
        include_fk = True