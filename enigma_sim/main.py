from classes import Enigma
#Debugging
x = Enigma([1, 2, 3])
x.rotors[2].position = 0
x.rotors[1].position = 0
x.rotors[0].position = 3

print(x.encrypt('ABCDEABCDEABCDEABCDEABCDE'))
