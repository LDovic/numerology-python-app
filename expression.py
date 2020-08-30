import string
from reduce import get_input
from reduce import numerologize

alphabet = list(string.ascii_lowercase)

name = get_input('full name')	

def calc(name):
	x = 0
	for letter in list(name):
		if letter.lower() in alphabet:
			x += alphabet.index(letter.lower()) + 1
	print(numerologize(x, True))
calc(name)
