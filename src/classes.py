from dictionaries import *

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


class Enigma:
	def __init__(self):
		self.crosover = DefaultCrossover
		self.reflector = DefaultReflector
		self.rotorsNumbers = [1, 2, 3]
		self.numberOfRotors = len(self.rotorsNumbers)
		self.rotors = []

		for i in self.rotorsNumbers:
			self.rotors.append(Rotor(i-1))


	def encrypt(self,char):

		char.set(self.crosover[char.letter])

		char.set(self.rotors[2].encrypt(char))
		char.set(self.rotors[1].encrypt(char, False, False, self.rotors[2]))
		char.set(self.rotors[0].encrypt(char, False, False, self.rotors[1]))
		
		char.set(self.reflector[char.letter])

		char.set(self.rotors[0].encrypt(char, True, True))
		char.set(self.rotors[1].encrypt(char, True, True))
		char.set(self.rotors[2].encrypt(char, True, True))

		char.set(self.crosover[char.letter])

		return char
