#1
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat = Bengal("Kitty", 1)
chartreux_cat = Chartreux("Catty", 3)
siamese_cat = Siamese("Fluffy", 5)

cats = [bengal_cat, siamese_cat, chartreux_cat]

my_cats = Pets(cats)
my_cats.walk()

#2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        self_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if self_strength > other_strength:
            return f"{self.name} wins the fight"
        elif self_strength < other_strength:
            return f"{other_dog.name} wins the fight"
        else:
            return "The dogs are equally strong"
        
dog = Dog("Matt", 5, 15)
doggo = Dog("Dymok", 2, 12)
puppy = Dog("Sam", 1, 20)

print(dog.bark())
print(dog.run_speed())
print(dog.fight(doggo))

#4
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs["name"]}is born")
        # print(f"Congratulations! {kwargs}is born")

    def is_18(self, name):
        for m in self.members:
            if m["name"] == name:
                return m["age"] >= 18
            
    def family_presentation(self):
        print(f"The family's last name is {self.last_name}")
        for m in self.members:
            print(m)

choens = Family("Choen", [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ])

choens.born(name='Kate', age=0, gender='Female', is_child=True)

print(choens.is_18('Kate'))
print(choens.is_18('Michael'))

choens.family_presentation()

#5
class TheIncredibles(Family):
    def use_power(self, name):
        for m in self.members:
            if m["name"] == name:
                if m["age"] > 18:
                    print({m["power"]})
                else: 
                    raise Exception(f"{name} is not over 18 years old")
                
    def incredible_presentation(self):
        print("*Here is our powerful family **")
        super().family_presentation()

incredibles = TheIncredibles("Incredibles", [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ])

incredibles.incredible_presentation()
incredibles.born(name='Jack', age=0, gender='male', is_child=True, power= 'Unknown Power')
incredibles.incredible_presentation()