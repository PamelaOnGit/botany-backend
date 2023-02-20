from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from models.customer import CustomerModel
from serializers.customer import CustomerSchema
from middleware.secure_route import secure_route

customer_schema = CustomerSchema()

router = Blueprint('customers', __name__)

# CUSTOMER_TABLE ENDPOINTS
# -----------------------

# get all customers 
@router.route("/customers/all", methods=["GET"])
@secure_route
def get_customers(): 
    customers = CustomerModel.query.all() 
    return customer_schema.jsonify(customers, many=True)

# add a customer
@router.route("/customer", methods=["POST", "PATCH"])
def add_customer(): 
    customer_dictionary = request.json
    
    try: 
        customer = customer_schema.load(customer_dictionary)
        customer.save()
        return customer_schema.jsonify(customer), HTTPStatus.CREATED
    except ValidationError as e: 
        return { "errors": e.messages, "message": "Something went wrong" }
#         # TODO handle integrity errors
#         # TODO only add customers if customer email is not unique - 
#         # TODO otherwise, update customer details with PATCH

#  find a customer by id
@secure_route
@router.route("/customer/find_id/<int:customer_id>", methods=["GET"])
def find_customer_by_id(customer_id):
    existing_customer = CustomerModel.query.get(customer_id)
    if not existing_customer: 
        return { "message": "customer not found" }, HTTPStatus.NOT_FOUND
    try: 
        return customer_schema.jsonify(existing_customer)
    except ValidationError as e: 
        return {"errors": e.messages, "message": "Something went wrong"}


# find a customer by email
# !
@router.route("/customer/find", methods=["GET"])
@secure_route
def get_customer_by_name(): 
    customer_email = request.json
    existing_customer = CustomerModel.query.filter(
        CustomerModel.email.like(customer_email["email"])
    )
    if not existing_customer: 
        return { "message": "customer not found" }, HTTPStatus.NOT_FOUND
    try: 
        return customer_schema.jsonify(existing_customer, many=True)
    except Exception as e: 
        return {"errors": e.messages, "message": "Something went wrong"}

# TODO add a customer billing address 
# @router.route("/customers/billing_address", methods=["POST"])
# def add_billing_address(): 
#     billing_address_dictionary = request.json
#     return customer_billing_address
  


