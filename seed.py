
from app import app, db 
from models.product import ProductModel
from models.image import ImageModel
from models.category import CategoryModel
from models.order_status import OrderStatusModel
from models.billing_address import BillingAddressModel
from models.delivery_address import DeliveryAddressModel
from models.customer import CustomerModel
from models.delivery_option import DeliveryOptionModel
from models.order import OrderModel
from models.order_line import OrderLineModel
from models.customer_billing_address import CustomerBillingAddressModel



with app.app_context(): 
    
    try: 
        print('Creating our database... ')
        # ! seeding will remove all information from the database
        db.drop_all()
        db.create_all()
        print('Seeding the database...')

        

        test_customer = CustomerModel(first_name="Dotty", last_name="Smith", title="Mrs", email="dotty@gmail.com", phone="+123456789")
        db.session.add(test_customer)
        db.session.commit()

        test_delivery_option = DeliveryOptionModel(name="next-day")
        db.session.add(test_delivery_option)
        db.session.commit()

        test_delivery_address = DeliveryAddressModel(name = "Mr M James", street_address="2, Fairfax Road", city="Birmingham", region="", postcode="BH14 9HM")
        db.session.add(test_delivery_address)
        db.session.commit()

        test_billing_address = BillingAddressModel(customer_id=test_customer.id, street_address="1, Oaktree Lane", city="London", region="", postcode='SW1 2AA')
        db.session.add(test_billing_address)
        db.session.commit()

        test_customer_billing_address = CustomerBillingAddressModel(customer_id=test_customer.id, billing_address_id=test_billing_address.id)
        db.session.add(test_customer_billing_address)
        db.session.commit()

        test_order_status = OrderStatusModel(name="created")
        db.session.add(test_order_status)
        db.session.commit()

        test_category = CategoryModel(name="kokedama")
        db.session.add(test_category)
        db.session.commit()

        test_order = OrderModel(customer_id=test_customer.id, delivery_address_id=test_delivery_address.id, delivery_option_id=test_delivery_option.id, total_amount=10.00, order_status_id=test_order_status.id)
        db.session.add(test_order)
        db.session.commit()

        test_product = ProductModel(name = "sunrise", category_id = test_category.id, alt_name = "kokedama - Japanese", price = 30, image = "image string", long_description = "some text long", short_description = "some text short", in_stock = 5)
        db.session.add(test_product)
        db.session.commit()

        test_order_line = OrderLineModel(order_id=test_order.id, product_id=test_product.id, quantity=1, gift=True, message="some optional string", option="some string describing the base")
        db.session.add(test_order_line)
        db.session.commit()
        print(test_product.id)

        test_image = ImageModel(image_url="some url as Text", product_id=test_product.id)
        test_image.save()

        print("Database seeded!")
    except Exception as e: 
        print(e)

        