import unittest, sys
sys.path.append('..')
from classes import *

class TestMarkdownPy(unittest.TestCase):

	def test_enigma_encryption(self):
		enigma = Enigma([1, 2, 3])
		enigma.rotors[2].position = 2
		enigma.rotors[1].position = 10
		enigma.rotors[0].position = 3
		self.assertEqual(
				enigma.encrypt('ABcdeFGHijklmnoprstUUUUUUUUz'),
				'LZPPUPETPKXDQRSXGVLKGBXMLQPF')
	def test_exceptions(self):
		with self.assertRaises(ValueError):
			enigma = Enigma([1, 2, 3])
			enigma.encrypt(23)
		with self.assertRaises(ValueError):
			rotor = Rotor(1)
			rotor.encrypt(23)

	def test_repr(self):
		char = Char('F')
		self.assertEqual(
				char.__repr__(),
				('F')
				)
		char = Char(0)
		self.assertEqual(
				char.__repr__(),
				('A')
				)

if __name__ == '__main__':
	unittest.main()
