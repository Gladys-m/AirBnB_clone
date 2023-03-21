#!/usr/bin/python3

"""
The base model defines all common attributes/methods for other classes
"""

import uuid #automatically generates unique Ids
from datetime import datetime

class BaseModel:
	"""The BAsemodel class"""

	def __init__(self, *args, **kwargs):
		"""Intitializes the Basemodel class"""
		if kwargs:
			for key, value in kwargs.items():
				if key == 'created_at' or key == 'updated_at':
					value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
				if key != '__class__':
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()

	def __self__(self):
		"""A method that returns the string representation of the Basemodel instance"""
		return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

	def save(self):
		"""A method that updates the updated_at attribute with the current date"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""A method that returns a dictionary containing all keys and values of the intsance"""
		new_dict = self.__dict__.copy()
		new_dict['__class__'] = type(self).__name__
		new_dict['created_at'] = self.created_at.isoformat()
		new_dict['updated_at'] = self.updated_at.isoformat()
		return new_dict
