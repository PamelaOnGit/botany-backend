from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from models.product import ProductModel
from serializers.product import ProductSchema

from models.image import ImageModel
from serializers.image import ImageSchema

product_schema = ProductSchema()
image_schema = ImageSchema()

router = Blueprint('kokedamas', __name__)

# PRODUCT_TABLE ENDPOINTS
# ----------------------

# get all the products
@router.route("/kokedamas/all", methods=["GET"])
def get_products():
    products = ProductModel.query.all()
    return product_schema.jsonify(products, many=True)

# filter products by in_stock property
# ! Check this .query.filter method - there might be a better or updated one
@router.route("/kokedamas", methods=["GET"])
def get_stock(): 
    products_stock = ProductModel.query.filter(ProductModel.in_stock!=0).all()
    return product_schema.jsonify(products_stock, many=True)

# add a product
@router.route("/kokedamas", methods=["POST"])
def add_product():
    product_dictionary = request.json
    try:
        product = product_schema.load(product_dictionary)
        product.save()
        return product_schema.jsonify(product), HTTPStatus.CREATED
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
            # TODO look up integrity errors, if image fails to save

# delete a product
@router.route("/kokedamas/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    existing_product = ProductModel.query.get(product_id)
    if not existing_product:
        return {"message": "No product found"}, HTTPStatus.NOT_FOUND
    existing_product.remove()
    return '', HTTPStatus.NO_CONTENT

# update a product
@router.route("/kokedamas/<int:product_id>", methods=["PUT", "PATCH"])
def update_product(product_id):
    product_dictionary = request.json
    existing_product = ProductModel.query.get(product_id)
    if not existing_product:
        return {"message": "No product found"}, HTTPStatus.NOT_FOUND
    try:
      # TODO add permissions here: if existing_product.user_id != g.current_user.id:
      # TODO return { "message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        updated_product = product_schema.load(
            product_dictionary,
            instance=existing_product,
            partial=True
        )
        updated_product.save()
    except ValidationError as e: 
        return { "errors": e.messagess, "message": "Something went wrong"}
    return product_schema.jsonify(updated_product), HTTPStatus.OK


# get a single product by id
@router.route("/kokedamas/<int:product_id>", methods=["GET"])
def get_single_product(product_id):
    existing_product = ProductModel.query.get(product_id)
    if not existing_product:
        return {"message": "product not found"}, HTTPStatus.NOT_FOUND
    try:
        return product_schema.jsonify(existing_product)
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}


# IMAGES_TABLE ENDPOINTS
# ----------------------

# posting an image to images_table
@router.route("/kokedamas/<int:product_id>/gallery", methods=["POST"])
def add_image(product_id):
    image_dictionary = request.json
    existing_product = ProductModel.query.get(product_id)
    if not existing_product:
        return {"message": "product not found"}, HTTPStatus.NOT_FOUND
    try:

        image = image_schema.load(image_dictionary)
        image.product_id = product_id
        image.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
    # TODO look up integrity errors, if image fails to save
    print(image)
    return image_schema.jsonify(image), HTTPStatus.CREATED

# delete an image from the images_table
@router.route("/kokedamas/gallery/<int:image_id>", methods=["DELETE"])
def delete_image(image_id): 
    existing_image = ImageModel.query.get(image_id)
    if not existing_image: 
        return {"message": "image not found"}
    existing_image.remove()
    return '', HTTPStatus.NO_CONTENT

