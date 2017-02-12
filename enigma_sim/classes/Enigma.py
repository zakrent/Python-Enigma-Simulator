from .Rotor import *

class Enigma:
	def __init__(self, rotorsNumbers):
		self.crosover = DefaultCrossover
		self.reflector = DefaultReflector
		self.rotorsNumbers = rotorsNumbers
		self.numberOfRotors = len(self.rotorsNumbers)
		self.rotors = []

		for i in self.rotorsNumbers:
			self.rotors.append(Rotor(i-1))


	def encrypt(self,value):
		if type(value) == str:
			finalStr = ''
			for letter in value.upper():
				finalStr += self.encrypt(Char(letter)).letter
			return finalStr
		elif type(value) == Char:
			char = value
			char.set(self.crosover[char.letter])

			previousRotor = None
			for i in range(len(self.rotors)):
				char.set(self.rotors[len(self.rotors)-i-1].encrypt(char, False, False, previousRotor))
				previousRotor = self.rotors[len(self.rotors)-i-1]

			char.set(self.reflector[char.letter])

			for i in range(len(self.rotors)):
				char.set(self.rotors[i].encrypt(char, True, True))

			char.set(self.crosover[char.letter])

			return char
		else:
			raise ValueError('Enigma.encrypt() accepts only str or Char type')
