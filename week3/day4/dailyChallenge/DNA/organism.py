from dna import DNA
import random

class Organism:
    def __init__(self, dna=None, environment=0.1):
        self.dna = dna if dna else DNA()
        self.environment = environment  # Mutation probability

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()
