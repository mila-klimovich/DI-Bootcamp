#1
from datetime import datetime

def get_age(year, month, day):
    current_date = datetime.now()

    birth_date = datetime(year, month, day)
    age = current_date.year - birth_date.year
    
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1  
    
    return age

def can_retire(gender, date_of_birth):

    year, month, day = map(int, date_of_birth.split('/'))

    age = get_age(year, month, day)
  
    if gender == "m":
        retirement_age = 67
    elif gender == "f":
        retirement_age = 62  
    
    if age >= retirement_age:
        return True
    else:
        return False

def main():
    gender = input("Enter your gender (m/f): ").lower()
    date_of_birth = input("Enter your birthdate (yyyy/mm/dd): ")
    
    if can_retire(gender, date_of_birth):
        print("You can retire!")
    else:
        print("You cannot retire yet.")


main()

#2
def sum_of_numbers(X):
    X_str = str(X)
    XX = int(X_str * 2) 
    XXX = int(X_str * 3)  
    XXXX = int(X_str * 4)  
    
    return X + XX + XXX + XXXX

X = 3
result = sum_of_numbers(X)
print(result)

#3
import random
def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throws += 1
        if dice1 == dice2:  
            return throws
        
def main():
    results = []  
    total_throws = 0

    for _ in range(100):
        throws = throw_until_doubles()
        results.append(throws)
        total_throws += throws

    average_throws = total_throws / len(results)

    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()
