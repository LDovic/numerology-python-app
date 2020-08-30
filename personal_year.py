from reduce import get_input
from reduce import numerologize
from datetime import datetime

cyear = datetime.now().year

day_and_month = numerologize(get_input("birthday") + get_input("month"), False)
year = int(get_input("year"))

for x in range(year, cyear + 1):
	print(str(x) + ": " + str(numerologize(day_and_month + x))
