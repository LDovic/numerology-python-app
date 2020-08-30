from life_path import *
from expression import *
from personal_year import *
from challenge import *
from colors import *

print(bcolors.GREEN + "Welcome to the numerology terminal app" + bcolors.ENDC)

print(bcolors.BLUE + "According to Aristotle, the Pythagoreans used mathematics for solely mystical reasons, devoid of practical application. They believed that all things were made of numbers. The number one (the monad) represented the origin of all things and the number two (the dyad) represented matter. The number three was an 'ideal number' because it had a beginning, middle, and end and was the smallest number of points that could be used to define a plane triangle, which they revered as a symbol of the god Apollo. The number four signified the four seasons and the four elements. The number seven was also sacred because it was the number of planets and the number of strings on a lyre, and because Apollo's birthday was celebrated on the seventh day of each month. They believed that odd numbers were masculine, that even numbers were feminine, and that the number five represented marriage, because it was the sum of two and three." + bcolors.ENDC)

print("Press ")
print(bcolors.RED + "1" + bcolors.ENDC + " for the life path number")
print(bcolors.RED + "2 " + bcolors.ENDC + "for the expression number")
print(bcolors.RED + "3 " + bcolors.ENDC + "for the personal year number")
print(bcolors.RED + "4 " + bcolors.ENDC + "for the challenge numbers")


def get_file(number):
    try:
        number = int(number)
    except ValueError: 
        get_file(get_input(""))

    if number == 1:
        result = life_path()
    elif number == 2:
        result = expression()
    elif number == 3:
        result = personal_year()
    elif number == 4:
        result = challenge()
    else:
        get_file(get_input(""))

    if not isinstance(result, list):
        print(bcolors.BOLD + str(result) + bcolors.ENDC)
        return
    for r in result:
        print(bcolors.BOLD + str(r) + bcolors.ENDC)

get_file(get_input(""))

