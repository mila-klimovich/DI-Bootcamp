class Dog:
    def __init__(self, name, color, sound): #object method -- initializer -- always called when an instance is created
        # print("The dog has been initialized")
        self.name = name
        self.color = color
        self.sound = sound

    def speak(self): #every method needs to talk self as an argument
        print(f"{self.name} says {self.sound}")
    
    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters") #number of meters isnt attached to a dog, this needs to be passed when the method is called

    def aged(self):
        self.color = 'grey'

my_dog = Dog('Peanut', 'Dark Brown', "quack")
laras_dog = Dog('Mizette', 'Blue', "bark")

# my_dog.speak()
# laras_dog.speak()

# my_dog.walk(1500)
# laras_dog.walk(1500)

print(my_dog.color)
my_dog.aged()
print(my_dog.color)
                
# print(f"my dog {my_dog.name} is {my_dog.color}")
# print(f"Lara's dog {laras_dog.name} is {laras_dog.color}")


# Analyse the code below. What will be the ouput ?
# Explain the goal of the __init__() method
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)

# Analyse the code below. What will be the output ?
# Explain the goal of the methods
# Create a method that modifies the name of the person
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)
    
    def modify_name(self, new_name):
        print("Hello my new name is " + new_name)


first_person = Person("John", 36)
first_person.show_details()
first_person.modify_name("Pete")

# Analyse the code below. What will be the output ?

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"greetings {self.name}")

    def street_greet(self):
        print(f"hey {self.nickname}")

anna = Person('Anna')
anna.greet()
anna.nickname = 'An'
anna.street_greet()

anna.nickname = 'D SYS'
anna.street_greet()


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

milaAcct = BankAccount(1, 100)
marcusAcct = BankAccount(2, 950000)

milaAcct.withdraw(150)
marcusAcct.withdraw(2000)

milaAcct.deposit(100)
marcusAcct.deposit(20000)

milaAcct.view_transactions()
marcusAcct.view_transactions()