from reduce import get_input
from reduce import numerologize

def life_path():
    birthday = get_input("birthday")
    month = get_input("month")
    year = get_input("year")

    return numerologize(birthday + month + year, True)
