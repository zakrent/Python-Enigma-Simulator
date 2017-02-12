from classes import *
#Debugging
x = Enigma()
x.rotors[2].position = 0
x.rotors[1].position = 0
x.rotors[0].position = 3

print(x.encrypt('ABCDEABCDEABCDEABCDEABCDE'))
