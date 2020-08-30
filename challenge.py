from reduce import get_input
from reduce import numerologize

def challenge():
    bday = numerologize(get_input("birthday"), False)
    month = numerologize(get_input("month"), False)
    year = numerologize(get_input("year"), False)

    def subtract(first, second):
        sub = first - second
        if sub < 0:
            sub = second - first
        return sub

    first = subtract(bday, month)
    second = subtract(year, bday)

    challenge_numbers = []

    challenge_numbers.append("First challenge number: " + str(first))
    challenge_numbers.append("Second challenge number: " + str(second))
    challenge_numbers.append("Third challenge number: " + str(subtract(first, second)))
    challenge_numbers.append("Fourth challenge number: " + str(subtract(month, year)))

    return challenge_numbers
