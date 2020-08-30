import string
from reduce import get_input
from reduce import numerologize

def expression():
    name = get_input("name")

    alphabet = list(string.ascii_lowercase)

    x = 0

    for letter in list(name):
        if letter.lower() in alphabet:
            x += alphabet.index(letter.lower()) + 1

    return numerologize(x, True)
