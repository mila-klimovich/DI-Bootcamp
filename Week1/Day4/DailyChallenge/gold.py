from datetime import datetime

birthdate = input("Input you birthay in DD/MM/YYYY: ")


birthdate_obj = datetime.strptime(birthdate, "%d/%m/%Y")

today = datetime.today()

age = today.year - birthdate_obj.year

if today.month < birthdate_obj.month or (today.month == birthdate_obj.month and today.day < birthdate_obj.day):
    age -= 1

last_digit_of_age = age % 10

cake = f"""
       ___{'i' * last_digit_of_age}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

print(cake)
