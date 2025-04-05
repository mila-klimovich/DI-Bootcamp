from anagram_checker import AnagramChecker

word_list = AnagramChecker("sowpods.txt")

while True: 
    print("Im an anagram checker, bro")
    action = input("Please enter a word to check for anagrams or 'quit' to exit: ").lower()

    if action == "quit":
        print("You're out, bro")
        break

    if len(action.split()) > 1: 
        print("Error: Please enter only one word") 
        continue 

    if not action.isalpha(): 
        print("Error: Please enter only alphabetic characters") 
        continue

    if word_list.is_valid_word(action):
        print(f"Your word {action.upper()} is a valid word")

        anagrams = word_list.get_anagrams(action)
        if anagrams: 
            print(f"Anagrams for your word: {', '.join(anagrams)}") 
        else:
            print("No anagrams found for your word.")  
    else:
        print(f"{action.upper()} is not a valid word")