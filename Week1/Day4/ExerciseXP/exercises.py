#Exercise 1
my_fav_numbers = set()
my_fav_numbers.add(1)
my_fav_numbers.add(7)

print(my_fav_numbers)

my_fav_numbers.remove(7)
print(my_fav_numbers)

friend_fav_numbers = {3, 5, 8}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

#Exercese 2
tuple_of_int = (1, 2, 3, 4)
tuple_of_int = tuple_of_int + (6, 7) #this creates a new tuple. Adding to existing is impossible, since its immutable
print(tuple_of_int)

#Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
count = basket.count("Apples")
print(count)
basket.clear()
print(basket)

#Exercise 4
mixed_list = list()
num = 1.5

while num <= 5:
    mixed_list.append(num)
    if mixed_list.index(num) % 2 != 0:
        mixed_list[mixed_list.index(num)] = int(num)
    num += 0.5

print(mixed_list)

#Exercise 5 
numbers = range(1, 21)

for num in numbers:
    print(num)

for num in numbers:
    if numbers.index(num) % 2 == 0:
        print(num)

#Exercise 6
my_name = 'Mila'
users_name = ''

while users_name != my_name: 
    users_name = input('Enter your name ').capitalize()
# print(users_name)

#Exercise 7
fruits_input = input("Enter your favorite fruit, separated by a space: ").lower()
favorite_fruits = fruits_input.split()

new_input = input("Enter one more fruit ").lower()
if new_input in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit! Hope you enjoy!")

#Exercise 8
toppings = []

while True:
    topping = input("Please enter a pizza topping ").lower()
    if topping == 'quit':
        break
    toppings.append(topping)
    print(f'{topping} is added to your pizza')

print(toppings)
print(f'Total price of you pizza is {len(toppings) * 2.5 + 10} dollars')

#Exercise 9
age_input = input('Please enter a family member\'s age, separated by a space ')
family_age = age_input.split()
total = 0

for age in family_age:
    age = int(age)
    if 3 <= age <= 12:
        total += 10
    elif age > 12:
        total += 15

print(f'Total cost of the tickets are: {total}')

teenagers = ['Garry', 'Lloyd', 'Alice', 'Mia', 'John']
teenagers = [teenager for teenager in teenagers if not (16 <= int(input(f'{teenager}, please enter your age ')) <= 21)]

print(teenagers)

#Exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
sandwich_orders = [order for order in sandwich_orders if not order == "Pastrami sandwich"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'I made your {sandwich}')