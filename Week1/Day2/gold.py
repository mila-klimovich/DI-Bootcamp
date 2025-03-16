#Exercise 1
print("Hello, world!\n" * 4)
print("I love python\n" * 4)

#Exercise 2
month = int(input("Please enter a month (1 to 12) "))

if 3 <= month <= 5:
    print("Its spring!")
elif 6 <= month <= 8:
    print("Its summer!")
elif 9 <= month <= 11:
    print("Its autumn!")
elif month == 12 or month <= 2:
    print("Its winter!")
else: 
    print("Wrong number!")