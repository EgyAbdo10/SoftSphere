#!/usr/bin/python3
"""create the Tool model"""

from models.base_model import BaseModel

class Tool(BaseModel):
    """create tools instances"""
    def __init__(self, **kwargs):
        """
        instansiate a Tool instance
        and set all attribute passed of the form of kwargs
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
