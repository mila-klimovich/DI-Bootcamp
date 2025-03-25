#1
class Cat:
    def _init_(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

kitty = Cat("Kitty", 2)
catty = Cat("Catty", 5)
fluffy = Cat("Fluffy", 7)

def oldest_cat(*args):
    oldest = args[0]
    for cat in args:
        if cat.age > oldest.age:
            oldest = cat

    return oldest

oldest = oldest_cat(kitty, catty, fluffy)

print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

#2
class Dog:
    def _init_(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")

        
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!!")

davids_dog = Dog("Rex", 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else: 
    print(f"{sarahs_dog.name} is bigger")

#3
class Song:
    def _init_(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for l in self.lyrics:
            print(l)

stairway = Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()

#4
class Zoo:
    def _init_(self, zoo_name): 
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            # print(self.animals)
    
    def get_animals(self):
        print(self.animals)

    def animal_sold(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted = {}
        for animal in self.animals:
            if animal[0] not in sorted.keys():
                sorted[animal[0]] = [animal]
                print(sorted)
            else: 
                sorted[animal[0]].append(animal)
                print(sorted)
        

new_york_zoo = Zoo("New Your Zoo")
new_york_zoo.add_animal("Dog")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Elephant")
new_york_zoo.add_animal("Emu")
new_york_zoo.get_animals()
new_york_zoo.sort_animals()