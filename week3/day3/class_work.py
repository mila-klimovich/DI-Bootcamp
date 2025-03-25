# class Animal():
#     def __init__(self, name, num_legs, sound):
#         self.name = name
#         self.num_legs = num_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I go {self.sound}")
    
#     def fetch(self):
#         print("This animal goes fetch")

# class Dog(Animal):
#     # def bark(self):
#     #     print(f"{self.name} barked, WAF !")
#     # pass
#     def fetch(self):
#         print("Im a dog and I fetched a stick")

# prince = Dog('Prince', 4, "Waf")
# # prince.bark()
# prince.make_sound()
# prince.fetch()

# tippy = Dog('Tippy', 3, 'Woof')
# tippy.make_sound()
# # print(tippy.num_legs)
# tippy.fetch()

# ralph = Animal('Ralph', 2, 'squak')
# ralph.make_sound()
# ralph.fetch()

# # class Circle:
# #     color = "red"

# # class NewCircle(Circle):
# #     color = "blue"

# # nc = NewCircle
# # print(nc.color)

# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)

# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         super().__init__(type, number_legs, sound)
#         # Or : Animal.__init__(self,type, number_legs, sound)
#         # Or: self.type = type
#         # self.number_legs = number_legs 
#         # self.sound = sound
#         self.fetch_ball = fetch_ball

# barky = Dog("Dog", 4, "Bark", True)
# print(barky.number_legs)

# class Family:
#     def __init__(self, surname):
#         self.surname = surname

# class Child(Family):
#     def __init__(self, name, surname):
#         # self.surname = surname
#         super().__init__(surname)
#         self.name = name

# class Cousin(Family):
#     def __init__(self, surname):
#         # self.surname = surname
#         super().__init__(surname)
#         # self.name = name

# ilan = Child('Ilan', 'Sarbac')
# beatrice = Child('Beatrice', 'Sarbac')

# print(beatrice.surname)
# print(ilan.surname)

# markus = Cousin('Markus')

# class MyClass():
#     def func(self):
#         print("I'm being called from the Parent class")


# class ChildClass(MyClass):
#     def func(self):
#         print("I'm actually being called from the Child class")
#         print("But...")
#         # Calling the `func()` method from the Parent class.
#         super().func()

# my_instance_2 = ChildClass()
# my_instance_2.func()

# Try to recreate the class explained below:

# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

# We can create a class called BlockedDoor that inherits from the base class Door.

# We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.

# class Door:
#     def __init__(self, is_opened = True):
#         self.is_opened = is_opened

#     def open_door(self):
#         self.is_opened = True

#     def close_door(self):
#         self.is_opened = False

# class BlockedDoor(Door):
#     def __init__(self):
#         super().__init__(False)
    
#     def open_door(self):
#         raise ValueError("A blocked door cant be opened")
#     def close_door(self):
#         return super().close_door()
    
# myDoor = BlockedDoor()
# myDoor.open_door()


# class Computer():

#     def __init__(self):
#         self.name = "Apple Computer" # public
#         self.__max_price = 900 # private

#     def sell(self):            # public method
#         print(f"Selling Price: {self.__max_price}")
#         self.__sell()

#     def __sell(self):          # private method
#       print('This is private method')

#     def set_max_price(self, price):
#         self.__max_price = price

# c = Computer()

# c.sell()

# def age():
#     user_age = input("How old are you?\n>>> ")
#     #######
#     try:
#         user_age = int(user_age)
#         print("I AM AFTER USER_AGE")
#     except:
#         print("Your age is not a real age")
#         user_age = 0
#     #######
#     print(f"Next year, you will be {user_age+1} years old")

# age()
    
# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you?")
#     try:
#         userage = int(userage)
#         valid_flag = True
#     except:
#         print("Please enter a real age")

# print("Next year, your age will be",userage+1)

# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you?")
#     try:
#         userage    = int(userage)
#         valid_flag = True
#     except:
#         pass

# print("Next year, your age will be",userage+1)

# Given a list of numbers, write a function that returns the sum of every number. BUT you can have a malicious string inside the list.

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
sum = 0

for i in my_list:
    try:
        sum += i
    except:
        print("Not not a valid number")
    finally:
        print("iteration")

print(sum)