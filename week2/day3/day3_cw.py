from functools import reduce
# def say_hello(username):
#     print(f"Hello, {username}!")

# say_hello("Sam")
# say_hello("Markus")
# say_hello("Michael")
# say_hello("Ilan")

# def say_hello(username, language="RU"):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username) 
#     elif language == "RU":
#         print("Privet "+username) 
#     elif language == "HE":
#         print("Shalom "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello("Alex", "RU")
# say_hello("Anna", "SW")
# say_hello("Shalom", "HE")
# say_hello("Aaron", "EN")

# say_hello(language="FR", username="Sam")

# say_hello('Liudmila')
# say_hello('Reuben', 'HE')
# say_hello('Mikhail')
# say_hello('Daniel')

# fav_number = 12

# def my_func():
#     print("I put the func in function")
#     my_name = "George"
#     print(my_name)
#     print(fav_number)

# my_func()

# print(my_name)

def number_multiplier(a):
    return 17 * a

new_num = number_multiplier(9)

def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())

first, last = format_name("RICk", "mORTY")
print(first)
print(last)


# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

# For example:

def calculation(a, b):
    return a + b, a - b

res = calculation(40, 10)
print(res)

def greet_users(users):             # users should be a list
    for user in users:              # Because it's a list, we can loop through it
        print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

usernames = ["steve", "stan", "debbie"]
greet_users(usernames)
print(greet_users)


def args_processer(*args):
    for i in args:
        print(i**2)

args_processer(1,2,3,4,5)


def kwargs_processer(**kwargs):
    print(kwargs)

kwargs_processer(teacher = "aaron", student = "marcus")

def sample(name, age, *args, **kwargs):
    print(f"{name} went to the park. He is {age}")
    print(args)
    print(kwargs)

sample("brutus", 55)
sample("brutus", 55, "charlie", "Moscow")
sample("brutus", 55, "charlie", "Moscow", location = "Ramat Gan", utensil = "pen")

def check(a, b, c):
    print(a, b, c)

a = [1,2,3]
check(*a)

a = {'a':'Sarah', 'b':24, 'c': 180}
check(**a)

def upper_string(s):
    return s.upper()

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(upper_string, fruit)

print(list(map_object))
print(fruit)

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))


def sum_numbers(first, second):
    print(first)
    print(second)
    return first+second

my_list = [1, 3, 5, 7]
reduced_list = reduce(sum_numbers, my_list)

print(reduced_list)

# def upper_string(s):
#     return s.upper()

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s.upper(), fruit)

print(list(map_object))

# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(lambda s: s[0] == "A", fruit)

print(list(filtered_object))

def my_func(name, age, sunglasses):
    print(f"my name is {name}. My age is {age}. I like {sunglasses}")

my_func("Aaron", 455, True)

my = lambda name, age, sunglasses: f"my name is {name}. My age is {age}. I like {sunglasses}"

print(my("Aaron", 455, True))

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

short_names = filter(lambda x: len(x) <= 4, people)
# print(short_names)

display_name = map(lambda x: f"Hello {x}", short_names)
# print(display_name)

# print(list(display_name))

for greeting in list(display_name):
    print(greeting)