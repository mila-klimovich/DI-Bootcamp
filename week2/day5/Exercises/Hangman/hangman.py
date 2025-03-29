import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)  

body_parts = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']

guessed_word = ['*' for _ in word]  
guessed_letters = []  
attempts_left = 6  

def display_state():
    print("Current word: " + " ".join(guessed_word))
    print(f"Attempts left: {attempts_left}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print("Gallows: " + ", ".join(body_parts[:6 - attempts_left]))

while attempts_left > 0 and '*' in guessed_word:
    display_state()

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed the letter '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts_left -= 1

if '*' not in guessed_word:
    print("Congratulations! You guessed the word: " + "".join(guessed_word))
else:
    print("Game over! The correct word was: " + word)
