from ast import Del
from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from models.delivery_address import DeliveryAddressModel
from serializers.delivery_address import DeliveryAddressSchema

from models.order import OrderModel
from serializers.order import OrderSchema
from serializers.single_order import SingleOrderSchema

from models.order_line import OrderLineModel
from serializers.order_line import OrderLineSchema

from models.order_status import OrderStatusModel
from serializers.order_status import OrderStatusSchema

from middleware.secure_route import secure_route


delivery_address_schema = DeliveryAddressSchema()
order_schema = OrderSchema()
single_order_schema = SingleOrderSchema()
order_line_schema = OrderLineSchema()
order_status_schema = OrderStatusSchema()

router = Blueprint('orders', __name__)


# ORDER ENDPOINTS
# ______________

# get all the orders
@router.route("/orders/all", methods=["GET"])
@secure_route
def get_orders():
    orders = OrderModel.query.all()
    print(orders)
    return order_schema.jsonify(orders, many=True)

# create a new order
@router.route("/order", methods=["POST"])
def create_order():
    order_dictionary = request.json
    # get customer_id from created customer after customer has been created
    # get delivery address_id from created delivery address after delivery_address is created
    order_dictionary["order_status_id"] = 1
    # add the new customer_id
    # add the new delivery_address_id
    # add the new delivery_option_id
    # add the total_amount from the form
    new_order = order_schema.load(order_dictionary)
    new_order.save()
    print(new_order.id)
    return order_schema.jsonify(new_order), HTTPStatus.CREATED

# get a single order by id
@router.route("/order/<int:order_id>", methods=["GET"])
@secure_route
def get_single_order(order_id):
    existing_order = OrderModel.query.get(order_id)
    if not existing_order: 
        return {"message": "order not found"}, HTTPStatus.NOT_FOUND
    try: 
        return single_order_schema.jsonify(existing_order)
    except ValidationError as e: 
        return { "errors": e.messages, "message": "something went wrong"}



# create a new delivery address
# TODO check whether delivery address exists before creating a new delivery address

# @router.route("/orders/delivery_addresses/all", methods=["GET"])
# def get_delivery_addresses():
#     addresses = DeliveryAddressModel.query.all()
#     return delivery_address_schema.jsonify(addresses, many=True)


@router.route("order/delivery_address", methods=["POST"])
def add_delivery_address():
    delivery_address_dictionary = request.json
    print(delivery_address_dictionary["street_address"])
    new_delivery_address = delivery_address_schema.load(delivery_address_dictionary)
    new_delivery_address.save()
    
    # ! I will need the new delivery address id for the order form
    print (new_delivery_address.id)
    return delivery_address_schema.jsonify(new_delivery_address), HTTPStatus.CREATED


# get all the delivery addresses
@router.route("orders/delivery_addresses/all", methods=["GET"])
def get_all_delivery_addresses(): 
    delivery_addresses = DeliveryAddressModel.query.all()
    return delivery_address_schema.jsonify(delivery_addresses, many=True)

# creating a new orderline for an order

@router.route("/order/orderline", methods=["POST"])
def add_order_line():   
    order_line_dictionary = request.json
    new_order_line = order_line_schema.load(order_line_dictionary)
    new_order_line.save()
    # add the order_id to the new order_line
    return order_line_schema.jsonify(new_order_line)

# update an order by order_id 
@router.route("/order/<int:order_id>", methods=["PUT", "PATCH"])
@secure_route
def update_order(order_id): 
    order_dictionary = request.json
    existing_order = OrderModel.query.get(order_id)
    if not existing_order: 
        return {"message": "order not found"}, HTTPStatus.NOT_FOUND
    try: 
        updated_order = order_schema.load(
            order_dictionary, 
            instance = existing_order, 
            partial=True
        )
        updated_order.save()
        return order_schema.jsonify(updated_order)
    except ValidationError as e: 
        return { "errors": e.messages, "message": "something went wrong"}
