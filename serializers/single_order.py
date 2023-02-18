from app import ma 
from models.order import OrderModel
from marshmallow import fields

class SingleOrderSchema(ma.SQLAlchemyAutoSchema):

    order_lines = fields.Nested("OrderLineSchema", many=True)
    customer = fields.Nested("CustomerSchema")
    delivery_address = fields.Nested("DeliveryAddressSchema")
    order_status = fields.Nested("OrderStatusSchema")

    class Meta: 
        model = OrderModel
        load_instance = True
        include_fk = True