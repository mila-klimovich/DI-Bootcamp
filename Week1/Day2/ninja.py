#Exercise 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

# without_a = "without"
# print("a" not in without_a)

longest_length = 0

while True: 
    without_a = input("Input the longest sentence you can without A ").lower()
    length = len(without_a)
    if length > longest_length and "a" not in without_a:
        longest_length = length
        print("Congratulations!")