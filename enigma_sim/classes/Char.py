from .dictionaries import *

class Char:
	def __init__(self, value):
		self.set(value)

	def set(self, value):
		if type(value) == int:
			self.number = value
		elif type(value) == str:
			self.number = CharToInt[value]

	@property
	def letter(self):
		return CharToInt[self.number]

	def __add__(self, value):
		return self.number + value
	def __sub__(self, value):
		return self.number - value
	def __repr__(self):
		return CharToInt[self.number]
