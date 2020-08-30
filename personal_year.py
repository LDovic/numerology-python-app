from reduce import get_input
from reduce import numerologize
from datetime import datetime

def personal_year():
   current_year = datetime.now().year

   day_and_month = numerologize(get_input("birthday") + get_input("month"), False)
   birth_year = int(get_input("year"))

   personal_year_list = []

   for year in range(birth_year, current_year + 1):
      personal_year_list.append(str(year) + ": " + str(numerologize(day_and_month + year, True)))

   return personal_year_list
