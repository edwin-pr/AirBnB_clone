#!/usr/bin/env python3
import uuid
from datetime import datetime
import models

class BaseModel:
    """
    The BaseModel class represents a base model for other data objects.

    Attributes:
        id (str): A unique identifier for the object.
        created_at (datetime): The date and time when the object was created.
        updated_at (datetime): The date and time when the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is provided, it updates object attributes based on the provided key-value pairs.
        Otherwise, it initializes the object with a new ID and current timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel object.

        Returns:
            str: A string representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute, saves the object, and stores it in the storage system.
        """
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel object.

        Returns:
            dict: A dictionary containing object attributes and metadata.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
