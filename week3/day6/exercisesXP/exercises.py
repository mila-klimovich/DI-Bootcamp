#1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if type(other) == Currency:
            if self.currency != other.currency:
                raise TypeError(f"Cannot add <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif type(other) == int:
            return Currency(self.currency, self.amount + other)

    def __iadd__(self, other):
        if type(other) == Currency:
            if self.currency != other.currency:
                raise TypeError(f"Cannot add <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif type(other) == int:
            self.amount += other
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  
print(int(c1))  
print(repr(c1)) 
print(c1 + 5)  
print(c1 + c2)  
print(c1)  
c1 += 5
print(c1) 
c1 += c2
print(c1)  

try:
    print(c1 + c3) 
except TypeError as e:
    print(e)  

#3
import random
import string

def random_string():
    letters = string.ascii_letters  
    random_string = ''.join(random.choice(letters) for _ in range(5))
    return random_string

s = random_string()
print(s)


#4
import datetime
def current_date():
    today = datetime.datetime.now().date()
    print(today)

current_date()

#5
def time_to_january_1st():
    current_date = datetime.datetime.now()

    january_1st = datetime.datetime(current_date.year + 1, 1, 1)

    time_difference = january_1st - current_date
    days_left = time_difference.days

    hours_left, remainder = divmod(time_difference.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)

    print(f"The 1st of January is in {days_left} days, {hours_left}:{minutes_left}:{seconds_left} hours.")

time_to_january_1st()

#6
def minutes_lived(birthdate):
    current_time = datetime.datetime.now()
    time_difference = current_time - birthdate
    minutes = time_difference.total_seconds()
    print(f'You have lived {int(minutes)} minutes.')

minutes_lived(datetime.datetime(1989, 10, 28))

#7
from faker import Faker

fake = Faker()
users = []

def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

for _ in range(10):  
    add_user()

for user in users:
    print(user)