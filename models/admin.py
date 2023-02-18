from datetime import datetime, timedelta

from app import db, bcrypt
from models.base import BaseModel
from sqlalchemy.ext.hybrid import hybrid_property
import jwt

from config.environment import secret

class AdminModel(db.Model, BaseModel):
    __tablename__ = "admin_table"

    username = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)

    # this method is going to pass
    # I am going to use a decorator
    # called hybrid property
    # it is a virtual column that will only exist before we save
    # it will not be a real column in the database

    @hybrid_property
    def password(self):
        pass

    # this method will se the password_hash to be a hashed version 
    # of the password
    # BEFORE it is saved to the database
    # this will be run before saving
    @password.setter
    def password(self, password_plaintext):
        # This will hash my password, then encode it for me
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_pw.decode("utf-8")

    def validate_password(self, password_plaintext):
        return bcrypt.check_password_hash(self.password_hash, password_plaintext)

    def generate_token(self):
        payload = { 
            "exp": datetime.utcnow() + timedelta(days=1), 
            "iat": datetime.utcnow(),
            "sub": self.id  #! this is the id of the user, which we can use later
        }

        token = jwt.encode(
          payload,
          secret, # ! Secret string only I know
          algorithm="HS256"
        )

        return token