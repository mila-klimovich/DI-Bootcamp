#1
animals1 = ["cat", "dog", "rabbit"]
animals2 = ["goat", "cow", "pig"]

animals1.extend(animals2)
print(animals1)

#2
for i in range(1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

#3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Please enter your name: ")

if user_name in names:
    i = names.index(user_name)
    print(i)
else:
    print("The name isnt in the list of names")

#4
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
third_num = int(input("Please enter the third number: "))

max_num = max(first_num, second_num, third_num)
print(max_num)

#5
letters = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiouy"

for l in letters:
    if l in vowels:
        print(f"{l} is a vovel")
    else:
        print(f"{l} is a consonant")

#6
seven_words = [input(f"Please enter a word number {i + 1}: ") for i in range(7)]

letter = input("Please enter a letter: ")

for s in seven_words:
    i = seven_words.find(letter)  # Ищем индекс первого вхождения буквы
    if i != -1:
        print(i)
    else:
        print(f"There's no letter {letter} in the word {s}.")
        
#7
numbers = list(range(1, 1000001))

print({min(numbers)})
print({max(numbers)})

total = sum(numbers)
print({total})

#8
numbers = input("Please enter numbers separated by ',':  ")

numbers_list = numbers.split(",")
numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)

#9
import random 

wins = 0  
losses = 0 

while True:
    user_input = input("Enter a number from 1 to 9 or 'quit' to exit:  ")
    
    if user_input.lower() == "quit":  
        break  
    
    user_number = int(user_input)  
    
    if user_number < 1 or user_number > 9:
        print("number should be from 1 to 9!")
        continue

    random_number = random.randint(1, 9) 

    if user_number == random_number:
        print("Winner!")
        wins += 1 
    else:
        print(f"Better luck next time!")
        losses += 1  

print(f"Total wins: {wins}, total loses: {losses}")

#Ninja1
import math  

C = 50
H = 30
res = []

ds = input("Please enter numbers splitted by commas: ")

numbers = ds.split(",")

for n in numbers:
    D = int(n)  
    Q = math.sqrt((2 * C * D) / H)
    res.append(str(int(Q))) 

print(",".join(res))

#Ninja2
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

print("The list of numbers: ", numbers)

sorted_numbers_desc = sorted(numbers, reverse=True)
print("The list sorted in descended order: ", sorted_numbers_desc)

sum_numbers = sum(numbers)
print("The sum of all the numbers is: ", sum_numbers)

first_last = [numbers[0], numbers[-1]]
print("The first and last numbers are: ", first_last)

greater_than_50 = [num for num in numbers if num > 50]
print("Numbers greater that 50: ", greater_than_50)

less_than_10 = [num for num in numbers if num < 10]
print("Numbers less than 10: ", less_than_10)

squared_numbers = [num ** 2 for num in numbers]
print("Squared numbers: ", squared_numbers)

unique_numbers = list(set(numbers))
print("Unique numbers: ", unique_numbers)
print("Qty unique numbers: ", len(unique_numbers))

average = sum_numbers / len(numbers)
print("The average of all numbers: ", average)

largest_number = max(numbers)
print("Max number: ", largest_number)

smallest_number = min(numbers)
print("Min number: ", smallest_number)

#Ninja3
import re

paragraph = "A partial eclipse of the Sun took place on Saturday morning. Pictures from across the world - from the UK to Spain, from Greenland to Senegal - show the progress of the Moon as it moved between the Earth and the Sun. Depending where you are, the partial eclipse looked as if the Moon was taking a nibble or a gigantic bite out of the Sun."

characters = len(paragraph)
print(f"Total number of characters (including spaces): {characters}")

sentences = re.split(r'[.!?]', paragraph.strip())
total_sentences = len(sentences)
print(f"Total number of sentences: {total_sentences}")

words = paragraph.lower().split()
total_words = len(words)
print(f"Total number of words: {total_words}")

unique_words = set(words)
unique_words = len(unique_words)
print(f"Total number of unique words: {unique_words}")

#Ninja4
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

words = text.split()

dict_words = {}

for word in words:
    if word in dict_words:
        dict_words[word] += 1
    else:
        dict_words[word] = 1

for word, fr in dict_words.items():
    print(f"{word}:{fr}")
