import random
#1
def display_message(): 
    print("in this course im learning Python for data analysis")

display_message()

#2
def favorite_book(title):
    print(f"One of my favorite book is {title}")

favorite_book("Master and Margarita")

#3
def describe_city(city, country = "Russia"):
    print(f"{city} is in {country}")
          
describe_city("Moscow")

#4
def compare_numbers(num_one):
    num_two = random.randint(1, 100)

    if 1 <= num_one <= 100:
        if num_one == num_two:
            print("Success!")
        else:
            print(f"Failed! Random number is {num_two} and you entered {num_one}")
    else:
        print("The number should be between 1 and 100")

input_num = int(input("Enter a number between 1 and 100 "))
compare_numbers(input_num)

#5
# def make_shirt(size, text):
#     print(f"The size of the shirt is {size} and the text is \"{text}\"")

# make_shirt("large", "Hurray")
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is \"{text}\"")

make_shirt()
make_shirt("medium")
make_shirt("small", "hohoho")
make_shirt(text="I eat apples", size="XXXL")

#6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)

def make_great():
    global magician_names
    magician_names = ["The Great " + magician for magician in magician_names]

make_great()
show_magicians()

#7
def get_random_temp(season):
    # return random.randint(-10, 40) 
    if season == "winter":
        return round(random.uniform(-35, 0), 1)
    elif season == "spring":
        return round(random.uniform(1, 19), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(2,19), 1)
    else:
        print("Invalid season")

# print(get_random_temp()) 

def main():
    # season = input("Please enter a season: ").lower()
    month = int(input("Please enter a month: "))

    if 12 <= month <= 2:
        season = "winter"
    elif 3 <= month <= 5:
        season = "spring"
    elif 6 <= month <= 8:
        season = "summer"
    elif 9 <= month <= 11:
        season = "summer"
    else:
        print("Invalid month")

    current_temp = get_random_temp(season)
    print(f"The temperature right now is {current_temp} degrees Celsius.")

    if current_temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 <= current_temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= current_temp <= 23:
        print("It's nice and warm outside, enjoy!")
    elif 24 <= current_temp < 32:
        print("It's quite hot, go to the beach and enjoy!")
    elif 32 <= current_temp < 40:
        print("Its too hot, stay home!")

main()

#8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_user(data):
    right_answers = 0
    wrong_answers = 0
    wrong_answers_list = []

    for item in data:
        question = item["question"]
        right_answer = item["answer"].lower()
        
        users_answer = input(f"Please enter your answer to {question} ").lower()
        
        if users_answer == right_answers:
            right_answers += 1
        else:
            wrong_answers += 1
            wrong_answers_list.append(f"To question {question} the right answer is {right_answer} and your answer was {users_answer}")

    return right_answers, wrong_answers, wrong_answers_list

def inform_user(right_answers, wrong_answers, wrong_answers_list):
    print(f"You gave {right_answers} correct answers, {wrong_answers} wrong answers")

    if wrong_answers_list:
        for i in wrong_answers_list:
            print(i)
    
    if wrong_answers > 3:
        print("Play again")

right_answers, wrong_answers, wrong_answers_list = ask_user(data)
inform_user(right_answers, wrong_answers, wrong_answers_list)