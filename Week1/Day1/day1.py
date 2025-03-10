print(type("45"))

print(45 + 5)

print("Hello Data People".replace("Data", "Full Stack"))

description = "strings are ..."
print(description.upper())
print(description.replace("are", "is"))
print(description[0:7])

my_age = 96
print(my_age + 123978)

#type casting

bank_balance = '121545'
phone_number = 154565

print(type(bank_balance))
print(type(phone_number))


print(int(bank_balance))
print(str(phone_number))

first_name = "Mila"
last_name = "Klimovich"
print(first_name, last_name)

print("Hello world!\nMy name is Mila")
print("Hello world!\tMy name is Mila")

print("The cow says, \"moo\"")

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

print(x < y and y > z)
print(word1 != word2)
print(bool(z))
print(bool(word1))

name = "Mila"
age = 30
city = "New York"

print(f"Hello, {name}! You're {age} yo and live in {city}")

# next_week = input("What do you want to do next week? ")
# print(f"you want to do {next_week} next week")

# age = int(input("How old are you? "))
# print(f"you are {age + 1} yo next year")

# my_height = int(input("How tall are you? "))

# if my_height > 200:
#     print("You are too tall to ride!")
# elif my_height < 150: 
#     print("You are too short!")
# else:
#     print("Enjoy the ride!")

# if my_height < 150 or my_height > 200:
    # print("you can't ride")
# else:
    # print("enjoy the ride")

print("A" in "ABCD")

num = int(input("type the number "))

if num % 15 == 0:
    print('FizzBuzz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0:
    print('Fizz')
else: 
    print('neither')