
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
from models.admin import AdminModel

with app.app_context():

    try:
        print('Creating our database... ')
        # ! seeding will remove all information from the database
        db.drop_all()
        db.create_all()
        print('Seeding the database...')

        test_customer = CustomerModel(
            first_name="Dotty", last_name="Smith", title="Mrs", email="dotty@gmail.com", phone="+123456789")
        db.session.add(test_customer)
        db.session.commit()

        test_delivery_option = DeliveryOptionModel(name="next-day")
        db.session.add(test_delivery_option)
        db.session.commit()

        test_delivery_option_3to5 = DeliveryOptionModel(name="three_to_five")
        db.session.add(test_delivery_option_3to5)
        db.session.commit()

        test_delivery_option_collection = DeliveryOptionModel(name="collection")
        db.session.add(test_delivery_option_collection)
        db.session.commit()

        test_delivery_address = DeliveryAddressModel(
            name="Mr M James", street_address="2, Fairfax Road", city="Birmingham", region="", postcode="BH14 9HM")
        db.session.add(test_delivery_address)
        db.session.commit()

        test_billing_address = BillingAddressModel(
            customer_id=test_customer.id, street_address="1, Oaktree Lane", city="London", region="", postcode='SW1 2AA')
        db.session.add(test_billing_address)
        db.session.commit()

        test_customer_billing_address = CustomerBillingAddressModel(
            customer_id=test_customer.id, billing_address_id=test_billing_address.id)
        db.session.add(test_customer_billing_address)
        db.session.commit()

        test_order_status = OrderStatusModel(name="created")
        db.session.add(test_order_status)
        db.session.commit()

        order_status_2 = OrderStatusModel(name="rejected")
        db.session.add(order_status_2)
        db.session.commit()

        order_status_3 = OrderStatusModel(name="accepted")
        db.session.add(order_status_3)
        db.session.commit()

        order_status_4 = OrderStatusModel(name="paid")
        db.session.add(order_status_4)
        db.session.commit()

        order_status_5 = OrderStatusModel(name="cancelled")
        db.session.add(order_status_5)
        db.session.commit()

        order_status_6 = OrderStatusModel(name="shipped")
        db.session.add(order_status_6)
        db.session.commit()

        order_status_7 = OrderStatusModel(name="delivered")
        db.session.add(order_status_7)
        db.session.commit()

        order_status_8 = OrderStatusModel(name="refunded")
        db.session.add(order_status_8)
        db.session.commit()

        test_category = CategoryModel(name="kokedama")
        db.session.add(test_category)
        db.session.commit()

        test_category_base = CategoryModel(name="base")
        db.session.add(test_category_base)
        db.session.commit()

        test_category_kit = CategoryModel(name="kit")
        db.session.add(test_category_kit)
        db.session.commit()

        test_order = OrderModel(customer_id=test_customer.id, delivery_address_id=test_delivery_address.id,
                                delivery_option_id=test_delivery_option.id, total_amount=10.00, order_status_id=test_order_status.id)
        db.session.add(test_order)
        db.session.commit()

        test_product = ProductModel(name="Moth Orchid", category_id=test_category.id, alt_name="ga ran", 
                                    price=35,
                                    image="https://res.cloudinary.com/dylcc2ao7/image/upload/v1677578650/orchid1_zjtopt.jpg", 
                                    long_description="Leaves like swords arise, \nFerns, ancient green soldiers stand,\nForest's noble guard.", 
                                    short_description="Phalaenopsis, or moth orchids are the most popular indoor orchids, with exotic, long lasting flowers.", in_stock=5)
        db.session.add(test_product)
        db.session.commit()

        test_product1 = ProductModel(name="Sword Fern", category_id=test_category.id, alt_name="ken shida", price=25,
                                     image="https://res.cloudinary.com/dylcc2ao7/image/upload/v1677581396/fern4_1_ak2k5q.jpg", 
                                     long_description="some text long", 
                                     short_description="The sword fern is a lush evergreen plant with bright green, sword-shaped fronds.", in_stock=5)
        db.session.add(test_product1)
        db.session.commit()

        test_product2 = ProductModel(name="Ivy", category_id=test_category.id, alt_name="wandā", price=25,
                                     image="https://res.cloudinary.com/dylcc2ao7/image/upload/v1677578968/ivy2_cwuco9.jpg", 
                                     long_description="some text long", 
                                     short_description="Hedera helix, the common ivy or English ivy, is a versatile ivy with trailing stems that are laced with rich green, slightly ruffled leaves.", in_stock=5)
        db.session.add(test_product2)
        db.session.commit()

        test_order_line = OrderLineModel(order_id=test_order.id, product_id=test_product.id, quantity=1,
                                         gift=True, message="some optional string", option="some string describing the base")
        test_order_line.save()

        test_image = ImageModel(
            image_url="some url as Text", product_id=test_product.id)
        test_image.save()

        test_image2 = ImageModel(
            image_url="whatever it should be", product_id=test_product.id)
        test_image2.save()

        test_admin = AdminModel(username="Pam", password="password")
        test_admin.save()

        print("Database seeded!")
    except Exception as e:
        print(e)
