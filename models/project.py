#!/usr/bin/python3
"""create the Project model"""

from models.base_model import BaseModel


class Project(BaseModel):
    """create the Project model"""
    def __init__(self, **kwargs):
        """
        instansiate a Project instance
        and set all attribute passed of the form of kwargs
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
