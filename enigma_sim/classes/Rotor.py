from .Char import *
from .dictionaries import *

class Rotor:
	def __init__(self, rotorNumber):
		self.wiring = DefaultRotorDicts[rotorNumber]
		self.invWiring = {v: k for k, v in DefaultRotorDicts[rotorNumber].items()}
		self.position = 0
	def encrypt(self, char, noRotation = False, inverted = False, prevRotor = None):

		if not noRotation:
			if not prevRotor:
				self.position += 1
			elif prevRotor.position == prevRotor.wiring['Knock']:
				self.position += 1
			if self.position > 25:
				self.position = 0

		char.set( ((char + self.position) % 26) )

		if inverted:
			char.set(self.invWiring[char.letter])
		else:
			char.set(self.wiring[char.letter])

		char.set( ((char - self.position) % 26) )

		return char
