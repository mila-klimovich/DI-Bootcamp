#1
for i in range(1, 4, 2):
    print(' ' * (3 - i // 2) + '*' * i)

#2
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)

#3
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)

for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * i)

#4
my_list = [2, 24, 12, 354, 233]  # Initialize the list to be sorted.
for i in range(len(my_list) - 1):  # Loop through each element except the last one.
    minimum = i  # Assume the current element is the minimum.
    for j in range(i + 1, len(my_list)):  # Loop through the remaining elements to find the minimum.
        if(my_list[j] < my_list[minimum]):  # If the current element is smaller than the assumed minimum.
            minimum = j  # Update minimum index to the current one.
            if(minimum != i):  # If the minimum index has changed, swap the elements.
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)  # Print the sorted list.
