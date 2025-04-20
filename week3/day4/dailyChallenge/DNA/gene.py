import random

class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def mutate(self):
        self.value = 1 - self.value  # Flip 0 -> 1 or 1 -> 0

    def __repr__(self):
        return str(self.value)
