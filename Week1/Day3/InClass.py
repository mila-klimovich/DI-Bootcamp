fewd = ['beans', 'breadcrumbs', 'eggs', 'apples', 'milk']
print(sorted(fewd))

list = [5, 10, 15, 20, 25, 50, 20]

twenty_index = list.index(20)

list[twenty_index] = 200

print(list)

a_tuple = (10, 20, 30, 40)

a = a_tuple[0]
b = a_tuple[1]
c = a_tuple[2]
d = a_tuple[3]

print(a)
print(b)
print(c)
print(d)

new_list = ['gabi', 'markus', 'sharon', 'gabi', 'alex', 'gabi']
new_set_list = set(new_list)
print(new_set_list)
print(new_set_list)
print(new_set_list)
# new_set_list_list = list(new_set_list)
# print(new_set_list_list)

for num in range(10,22):
    print(num)


a_number  = 1

while a_number < 12:
    print(a_number)
    a_number += 1

print(bool(20))

active = True

while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")