from organism import Organism

def main():
    generation = 0
    organism = Organism(environment=0.2)

    while not organism.dna.is_all_ones():
        generation += 1
        organism.mutate()
        if generation % 1000 == 0:
            print(f"Generation {generation}... still evolving...")

    print(f"🎉 Success in generation {generation}!")
    print("Final DNA:")
    print(organism.dna)

if __name__ == "__main__":
    main()
