## Admin user stories

1. As an admin, I want to login and view all the products in my database so that I can see all the products
// GET all products

2. As an admin, I want to login and add a product to the database so that I can store a new product in the database
// CREATE a new product

3. As an admin, I want to login and add an image to my images_table, and attach it to specific product, so that I can store a gallery of images for each product
// POST a new image 

3. As an admin, I want to login and delete a product from the database so that I can remove products that I no longer want in the database
// DELETE a product by ID

4. As an admin, I want to login and update a product in the database so that I can change the image, name, price and/or description of a product in the database, so that I can change the product values in the database
// UPDATE product by ID

5. As an admin, I want the products to be displayed in the shop to be filtered by the in_stock property, so that I can display the products I currently have available
// GET products filtered by in_stock

6. As an admin, I want to recieve orders from my customers by email, including the products ordered, the customer name, customer id, the delivery address, the delivery notes, and the price of the order so that I can decide whether to accept the order, take payment, fill the order and dispatch it

7. As an admin, I want to login and view all the orders
// GET all orders

8. As an admin, I want to login and view a particular order by id, so that I can view a particular order
// GET a single order by id

8. As an admin, I want to login and view all orders filtered by order_status
// GET orders filtered by order_status not delivered or shipped 


## Visitor user stories

As a visitor, I want to view all the availble products in the shop so that I can see which product are currently available to order
// GET all products filtered by available products

As a visitor, I want to select a product so that I can view the selected product and view all the available information about it (the entire spec)
// GET a single product by ID
// GET images of that product from images by id 

As a visitor, I want to add a product to my basket so that I can keep a list of the products that I want to order

As a visitor, I want to view all the products in my basket so that I can view all the products that I want to order before I start the checkout process // should this be stored in local storage?  

As a visitor, I want to proceed to checkout in order to enter my details and generate an order form, containing my order, my name, delivery address, delivery notes and preferences and payment details. 

As a visitor, I want to submit my order on the website, and see a confirmation, so that I know that my order form has been submitted. 






