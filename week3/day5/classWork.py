# class Israeli:
#     prime_minister = "Bibi"
#     num_citizens = 0
#     def __init__(self, name):
#         self.name = name
#         Israeli.num_citizens += 1
#         self.__tz = Israeli.num_citizens

#     @property
#     def get_tz(self):
#         return f"{self.__tz} 7"

# liudmila = Israeli('Liudmila')
# gabby = Israeli('Gabby')
# ilan = Israeli('Ilan')
# other_ilan = Israeli('other_Ilan')
# daniel = Israeli('daniel')

# # other_ilan.get_tz()

# print(daniel.get_tz)
# daniel.__tz = 87

# print(daniel.__tz)

# daniel.get_tz()
# print(Israeli.prime_minister)

# hadriel = Israeli('Hadriel', 1)

# print(hadriel.name)
# print(hadriel.tz)
# print(hadriel.prime_minister)

# liudmila = Israeli('Liudmila', 2)

# # print(liudmila.name)
# # print(liudmila.tz)
# print(liudmila.prime_minister)

# Israeli.prime_minister = "LeBron"

# print(liudmila.prime_minister)

# class Male(Israeli):
#     def __init__(self, name, tz, is_male = True):
#         super().__init__(name, tz)
#         self.is_male = is_male
    
# sam = Male("sam", 3, True)
# print(sam.prime_minister)

# class Circle:
#     color = "red"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#        return Circle.color

# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)


# class Person:

#     used_names = set()

#     def __init__(self, name, age):
#         if name in self.used_names:
#             name = input("That name is taken. Enter another name: ")

#         self.name = name
#         self.age = age
#         self.used_names.add(name)

#     @classmethod
#     def fromYear(cls, name, birth_year):
#         THIS_YEAR = 2020
#         return cls(name, THIS_YEAR - birth_year)

#     @property
#     def professional_name(self):
#         return "Mr " + self.name
    
# sharon = Person("Sharon", 29)
# markus = Person("Markus", 40)

# print(Person.fromYear('Sharone', 1996))

# print(markus.professional_name)

# class MyClass:
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print(f"Value of object : {object_1.get_val()}")
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print(f"Value of object : {object_2.get_val()}")
# print(MyClass.get_count())

class Ilan:
    def __init__(self, coolness_level):
        self.coolness_level = coolness_level

    def __str__(self): #string representation of an instance
        return f"This Ilan has a coolness level of {self.coolness_level}"
    
    def __len__(self): #length of an instance
        return 6
    
    def __call__(self): #this what happens when we call instance as a function
        for i in range(self.coolness_level):
            print(f"im cool {i + 1} times")

    def __add__(self, *args): 
        self.coolness_level += sum(args)
        print("coolness level updated")
        return self.coolness_level
    
    def __iadd__(self):
        pass

# ilans = Ilan(8)

# # print(ilans)
# # print(len(ilans))

# ilans()

# ilans += 7
# ilans()

# print(dir(Ilan))

class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName


#Here we overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'

  def __repr__(self):

# We can write whatever we want inside this method, but we have to return an object.

      return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self,other):
      name = self.name[0] + other.name[1:]
      lastname = other.lastName
      return Person(name,lastname)

father = Person('John', 'Snow')
mother = Person('Kaleesi', 'MotherOfDragons')
# using the __add__() method
dragonChild = father + mother 

print(dragonChild)

# class PrintList(object):

#     def __init__(self, my_list):
#         self.mylist = my_list

#     def __repr__(self):
#         return str(self.mylist)


# printlist = PrintList(["a", "b", "c"])
# print(printlist.__repr__())

# from math import e as euler

# print(euler)

# # from faker import Faker
# # fake = Faker()
# # print(fake.date())

# import sys
# import typing

# from tabulate import tabulate

# def main(file1, file2):
#     file1_contents = extract_file_contents(file1)
#     file2_contents = extract_file_contents(file2)

#     display_files(file1_contents, file2_contents)

#     dates = sorted(set(file1_contents).union(file2_contents))
#     print(dates[len(dates) // 2])

# def display_files(file1_contents, file2_contents):
#     table = {
#         'file1': file1_contents,
#         'file2': file2_contents
#     }
#     print(tabulate(table))

# def extract_file_contents(file_path: str) -> typing.List[str]:
#     """ 
#     Extract file contents and strip whitespaces from each row.
#     : param file_path: The path to the file to extract
#     : return: A list of date data rows
#     """ 

#     with open(file_path, 'r') as f:
#         file_contents = f.readlines()
#     new_file_contents = []
#     for date_data_record in file_contents:
#         date_data_record = date_data_record.strip()
#         if date_data_record:
#             new_file_contents.append(date_data_record)
#     return new_file_contents

# if __name__ == '__main__':
#     args = sys.argv[1:]
#     if len(args) != 2:
#         print(f"Expected two arguments as files. Got {len(args)} instead.")
#         sys.exit(1)
#     main(*args)