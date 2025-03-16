#dictionaries arent ordered. A dictionary stores key-value pairs, where each unique key is an index which holds the value associated with it.

shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]

print(shirts[1]['price'])

# Access the value of key history


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])

# Delete set of keys from Python Dictionary

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# print(a_dict.items())
# # output : 
# dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

# The items() method returns a view object that displays 
# a list of dictionary's (key, value) tuple pairs.


for key, value in a_dict.items():
    print(key, '->', value)

# output
# color -> blue
# fruit -> apple
# pet -> dog 

sample_dict2 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict2[key]

print(sample_dict2)

my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for x, y in my_books.items():
    print("the " + x + " is " + y)

for (index_count, letter) in enumerate('abcd'):
    print(f'At index {index_count} the letter is {letter}')


for i in range(1, 3):
    print(i)
else:
    print('The for loop is over')


x = 0
while x < 2:
    print(f'x is {x}')
    x += 1
else:
    print('x is bigger than 2')


for letter in 'Leonardo':
    if letter == 'a':
        continue
    print(letter, end='\n')


my_number = '1234'

my_list = [int(num) * 2 for num in my_number]
print(my_list)

my_list = []
for num in my_number:
    my_list.append(int(num) * 2)
print(my_list)

my_list = [x for x in range(0,11) if x%2 == 0] # only even
print(my_list)

my_list = []

for i in [2, 3, 4]:
    for j in [100, 200, 300]:
        my_list.append(i*j)

print(my_list)

my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]
print(my_list)


family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
new_year = 1

new_family_age = {name: age+new_year for (name, age) in family_age.items()}
print(new_family_age)