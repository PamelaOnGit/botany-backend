from ast import Del
from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from models.delivery_address import DeliveryAddressModel
from serializers.delivery_address import DeliveryAddressSchema

from models.order import OrderModel
from serializers.order import OrderSchema

delivery_address_schema = DeliveryAddressSchema()
order_schema = OrderSchema()

router = Blueprint('orders', __name__)


# ORDER ENDPOINTS
# ______________

# get all the orders
@router.route("/orders/all", methods=["GET"])
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
    return order_schema.jsonify(new_order), HTTPStatus.CREATED


# create a new delivery address
# TODO check whether delivery address exists before creating a new delivery address

@router.route("/orders/delivery_addresses/all", methods=["GET"])
def get_delivery_addresses():
    addresses = DeliveryAddressModel.query.all()
    return delivery_address_schema.jsonify(addresses, many=True)


@router.route("orders/delivery_address", methods=["POST"])
def add_delivery_address():
    delivery_address_dictionary = request.json
    print(delivery_address_dictionary["street_address"])

    # # check if the delivery address already exists in the database
    # # if not, create new entry
    # existing_delivery_address = DeliveryAddressModel.query.filter(
    #   DeliveryAddressModel.street_address.like(delivery_address_dictionary["street_address"])
    # )
    # if not existing_delivery_address:
    #     new_delivery_address = delivery_address_schema.load(delivery_address_dictionary)
    #     new_delivery_address.save()
    # # ! I will need the new delivery address id for the order form
    #     print (new_delivery_address.id)
    #     return delivery_address_schema.jsonify(new_delivery_address), HTTPStatus.CREATED
    # return {"message": "this delivery address already exists"}

    new_delivery_address = delivery_address_schema.load(
    delivery_address_dictionary)
    new_delivery_address.save()
    # ! I will need the new delivery address id for the order form
    print (new_delivery_address.id)
    return delivery_address_schema.jsonify(new_delivery_address), HTTPStatus.CREATED


