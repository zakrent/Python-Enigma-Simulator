#!/usr/bin/python3
import unittest, sys
sys.path.append('..')
from classes import *

class TestMarkdownPy(unittest.TestCase):

	def test_enigma_encryption(self):
		enigma = Enigma()
		enigma.rotors[2].position = 2
		enigma.rotors[1].position = 10
		enigma.rotors[0].position = 3
		self.assertEqual(
					enigma.encrypt('ABcdeFGHijklmnoprstUUUUUUUUz'),
        			'LZPPUPETPKXDQRSXGVLKGBXMLQPF')

if __name__ == '__main__':
	unittest.main()
