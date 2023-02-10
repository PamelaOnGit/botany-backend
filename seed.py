
from app import app, db 
from models.product import ProductModel
from models.image import ImageModel




with app.app_context(): 
    
    try: 
        print('Creating our database... ')
        # ! seeding will remove all information from the database
        db.drop_all()
        db.create_all()
        print('Seeding the database...')
        
        test_product = ProductModel(name = "sunrise", category = "kokedama", alt_name = "kokedama - Japanese", price = 30, image = "image string", long_description = "some text long", short_description = "some text short", in_stock = 5)
        db.session.add(test_product)
        db.session.commit()

        print(test_product.id)

        image = ImageModel(image_url="some url as Text", product_id=test_product.id)
        image.save()

        print("Database seeded!")
    except Exception as e: 
        print(e)

        