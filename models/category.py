#!/usr/bin/python3
"""create the Category model"""

from models.base_model import BaseModel

class Category(BaseModel):
    """create Categories instances"""
    def __init__(self, **kwargs):
        """
        instansiate a Category instance
        and gives it a name
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
