class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, qty = 1):
        if animal not in self.animals:
            self.animals[animal] = qty
        else:
            self.animals[animal] += 1

    def get_animal_types(self):
        animal_list = sorted(self.animals.keys())
        return animal_list
    
    def get_short_info(self):
        types_of_animals = self.get_animal_types()
        info_animals = []

        for animal in types_of_animals:
            if self.animals[animal] > 1:
                info_animals.append(f"{animal}s")
            else:
                info_animals.append(animal)
        
        info = ", ".join(info_animals[0:-1]) + " and " + info_animals[-1]
        # print(info)
        return f"{self.name}'s farm has {info}"

mcdonald = Farm("MaDonald")

mcdonald.add_animal("cow")
mcdonald.add_animal("sheep", 2)
mcdonald.add_animal("goat", 12)
print(mcdonald.animals)

print(f"{mcdonald.name}'s farm")
for key, value in mcdonald.animals.items():
    print(f"{key} : {value}")

print("      E-I-E-I-0!")

print(mcdonald.get_animal_types())
print(mcdonald.get_short_info())