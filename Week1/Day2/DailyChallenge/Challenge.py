import random

# 1
string = input("Please enter a string ")

if len(string) < 10:
    print("string not long enough")
elif len(string) > 10:
    print("string too long")
else: 
    print("perfect string")

# # 2
print(string[0])
print(string[len(string)-1])

# # 3
construct = ""
for char in string:
    construct += char
    print(construct)

# 4
my_list = list(string)
random.shuffle(my_list)
print(''.join(my_list))
    

