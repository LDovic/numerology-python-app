from reduce import get_input
from reduce import numerologize

bday = numerologize(get_input("birthday"), False)
month = numerologize(get_input("month"), False)
year = numerologize(get_input("year"), False)

def func(first, second):
	sub = first - second
	if sub < 0:
		sub = second - first
	return sub

first = func(bday, month)
second = func(year, bday)

print("First challenge number: " + str(first))
print("Second challenge number: " + str(second))
print("Third challenge number: " + str(func(first, second)))
print("Fourth challenge number: " + str(func(month, year)))
