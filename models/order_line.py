from app import db 
from models.base import BaseModel 
# !


class OrderLineModel(db.Model, BaseModel): 
    __tablename__ = "order_line_table"

    order_id = db.Column(db.Integer, db.ForeignKey('order_table.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product_table.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    gift = db.Column(db.Boolean, nullable=False, default=False)
    message = db.Column(db.Text)
    option = db.Column(db.Text)

    products = db.relationship('ProductModel', back_populates='order_lines')
    # orders = db.relationship('OrderModel', backref='order_lines')

    # Relationships 

    # - order_table - many-(order line)-to-one(-order)

    # an orderline appears on exactly one order
    # a single order can have many orderlines

    #  product_table - one-(order line)-to-many(-product)
    # a single orderline contains exactly one product
    # a product can be associated with many orderlines 


