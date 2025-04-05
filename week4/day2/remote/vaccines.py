class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = [] 

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)

class Queue:
    def __init__(self):
        self.humans = [] 

    def add_person(self, person):
        if person.priority or person.age > 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        try:
            return self.humans.index(person)
        except ValueError:
            return None  

    def swap(self, person1, person2):
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)

        if idx1 is not None and idx2 is not None:
            self.humans[idx1], self.humans[idx2] = self.humans[idx2], self.humans[idx1]

    def get_next(self):
        if self.humans:
            return self.humans.pop(0)
        return None

    def get_next_blood_type(self, blood_type):
        for person in self.humans:
            if person.blood_type == blood_type:
                self.humans.remove(person) 
                return person
        return None

    def sort_by_age(self):
        self.humans.sort(key=lambda x: (not x.priority, -x.age))

    def rearrange_queue(self):
        i = 0
        while i < len(self.humans) - 1:
            person1 = self.humans[i]
            person2 = self.humans[i + 1]
            if set(person1.family).intersection(person2.family):
                for j in range(i + 2, len(self.humans)):
                    if not set(self.humans[i].family).intersection(self.humans[j].family):
                        self.humans[i + 1], self.humans[j] = self.humans[j], self.humans[i + 1]
                        break
            i += 1

human1 = Human('1', 'Mia', 23, False, 'O')
human2 = Human('2', 'Marisa', 19, True, 'A')
human3 = Human('3', 'Manuel', 25, False, 'B')
human4 = Human('4', 'Pablo', 20, False, 'AB')


human1.add_family_member(human2)  
human1.add_family_member(human3)


queue = Queue()
queue.add_person(human1)
queue.add_person(human2)
queue.add_person(human3)
queue.add_person(human4)

queue.rearrange_queue()

for human in queue.humans:
    print(human.name)
