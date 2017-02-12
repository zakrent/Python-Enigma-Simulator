from .Rotor import *

class Enigma:
	def __init__(self):
		self.crosover = DefaultCrossover
		self.reflector = DefaultReflector
		self.rotorsNumbers = [1, 2, 3]
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

			char.set(self.rotors[2].encrypt(char))
			char.set(self.rotors[1].encrypt(char, False, False, self.rotors[2]))
			char.set(self.rotors[0].encrypt(char, False, False, self.rotors[1]))

			char.set(self.reflector[char.letter])

			char.set(self.rotors[0].encrypt(char, True, True))
			char.set(self.rotors[1].encrypt(char, True, True))
			char.set(self.rotors[2].encrypt(char, True, True))

			char.set(self.crosover[char.letter])

			return char
		else:
			raise ValueError('Enigma.encrypt() accepts only str or Char type')
