# #1
number = int(input("Please enter a number "))
length = int(input("Please enter a length "))

my_list = []
for i in range(1, length + 1):
    my_list.append(number * i)

print(my_list)

#2
string = input("Please enter a string ")
new_string = string[0]

for i in range(1, len(string)):
    if string[i] != string[i - 1]:
        new_string += string[i]

print(new_string)