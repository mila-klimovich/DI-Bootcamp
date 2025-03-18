#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))

print(my_dict)

#2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total = 0

for key, value in family.items():
    if 3 <= value <= 12:
        total += 10
    elif value > 12:
        total += 15

print(total)

#3
zara = {
    'name': 'Zara', 
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton'], 
    'number_stores': 7000, 
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']
        }
    }

more_on_zara = {
    'creation_date': 1975, 
    'number_stores': 10000
}

zara['number_stores'] = 2

print(f"Zara cliens are {zara['type_of_clothes'][0]}, {zara['type_of_clothes'][1]} and {zara['type_of_clothes'][2]}")

zara['country_creation'] = 'Spain'

zara['international_competitors'].append("Desigual")

del zara['creation_date']
print(zara)

print(zara['international_competitors'][len(zara['international_competitors']) - 1])

print(zara['major_color']['US'])

print(len(zara))
print(zara.keys())

zara.update(more_on_zara)
print(zara)
print(zara['number_stores'])

#4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# users_one = {}
# for i in range(len(users)):
#     print(i)
#     users_one[users[i]] = i

# print(users_one)

users_new = {i: user for (user, i) in enumerate(users)}
users_new2 = {user: i for (user, i) in enumerate(users)}
print(users_new)
print(users_new2)

users_new3 = {i: user for (user, i) in enumerate(sorted(users))}
print(users_new3)