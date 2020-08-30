from reduce import get_input
from reduce import numerologize

print(numerologize(get_input("birthday") + get_input("month") + get_input("year"), True))
