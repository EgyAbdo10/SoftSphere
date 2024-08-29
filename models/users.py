#!/usr/bin/python3
"""create the User model"""


from models.base_model import BaseModel

class User(BaseModel):
    """create the user model"""
    def __init__(self, **kwargs):
        """
        instansiate a User instance
        and set all attribute passed of the form of kwargs
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
