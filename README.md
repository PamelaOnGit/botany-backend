# instructions

1. seeding is successful 
2. table plus is not working - no db called pam
3. built a serializer for the products
4. created a table for additional images - gallery - with a one-to-many relationship between products-and-images
5. however, encountered the horrible bug below
6. resolved
7. serializers and controller (inside my product controller) for my images (gallery)
8. product endpoints - GET all, CREATE one, DELETE one by ID, UPDATE one by ID, GET filtered by in_stock
9. image endpoints - GET images filtered by productID (FK), CREATE one image by ProductID (FK), DELETE one image by ProductID (FK)
## Bugs 

When I was programming the image model and seeding in this project, I had an error I didn't recognise: 
raise AttributeError(key)
AttributeError: columns

I read the error in order to understand where in my code I had introduced the error. I looked at the files that were named in the error, however, I had not made changes to any of these files and I could not understand, from my examination of the error and of my code, how the code I had written (the new ImageModel) was affecting these files.  

After examining the error and my code, I looked for this error on StackOverflow. At first glance there was nothing relevant to the code I was writing.  

I removed the code I had written since the code had broken (it was only a few lines) and added it again.  I identified the exact line of code that was causing the error - in the ProductModel class in models.product, when I added the relationship between the ProductModel and the ImageModel. However, I could not understand how this line of code was raising the error.

I remembered that I had been prompted to install marshmallow-sqlalchemy during this process. I checked my dependencies against an earlier version of my code (I had used the * operator in my pipfile so that my dependencies were updating automatically).  

I saw that sqlalchemy had updated to a new version. I changed it back to the previous version and found that my code now worked as intended.  

I will reconsider whether I want automatic upgrades for my dependencies.  From now on, I will consider picking fixed versions.  

