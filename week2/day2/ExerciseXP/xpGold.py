#1 #2 #3

birthdays = {
    "Melany": "1990/05/15",
    "Costa": "1955/07/25",
    "Charls": "1982/12/19",
    "Dana": "1988/03/11",
    "Eli": "2020/10/30"
}

print("You can look up the birthdays of the people in the list!")

new_name = input("Please enter a name you wish to add: ")
new_birthday = input(f"Please enter their bd in YYYY/MM/DD format: ")

birthdays[new_name] = new_birthday

name = input("Input a person: ")

if name in birthdays:
    print(f"The birthday of {name} is {birthdays[name]}")
else:
    print(f"Sorry, we dont have the birthday information for: {name}")


#4
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("Items and their prices:")
for item, price in items.items():
    print(f"The price of {item} is {price}.")

items_stock = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0
for item, data in items_stock.items():
    total_cost += data["price"] * data["stock"]

print(f"\nTotal cost to buy everything in stock: {total_cost}")

#Ninja
manufacturers_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, Honda, Volkswagen, Toyota"

manufacturers = manufacturers_str.split(", ")

print(f"Total number of manufacturers: {len(manufacturers)}")

print(f"Manufacturers in reverse order (Z-A): {sorted(manufacturers, reverse=True)}")

count_o = sum(1 for manufacturer in manufacturers if 'o' in manufacturer.lower())
print(f"Number of manufacturers with 'o' in their name: {count_o}")

count_i = sum(1 for manufacturer in manufacturers if 'i' not in manufacturer.lower())
print(f"Number of manufacturers without 'i' in their name: {count_i}")

unique_manufacturers = set(manufacturers)

print(f"Manufacturers without duplicates: {', '.join(unique_manufacturers)}")
print(f"Total number of unique manufacturers: {len(unique_manufacturers)}")