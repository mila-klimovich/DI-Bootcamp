from game import Game

def get_user_menu_choice():
    print("\nChoose:")
    print("1. Play a new game")
    print("2. Show results")
    print("3. Exit")
    choice = input("You choose (1/2/3): ").strip()
    while choice not in ['1', '2', '3']:
        choice = input("Enter 1, 2 or 3: ").strip()
    return choice

def print_results(results):
    print("\nGame results:")
    print(f"Wins: {results['win']}")
    print(f"Loses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == '3':
            print_results(results)
            break

if __name__ == "__main__":
    main()
