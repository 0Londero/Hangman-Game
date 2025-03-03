from game_logic import *
from user_interface import *

art()

while True:
    if not menu():
        break  # Exit if the user chooses not to play

    encrypted_word, guessed_letters, attempts = play_hangman()  # Get returned values
    print("\nCurrent word:", encrypted_word)
    print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
    print("Incorrect guesses remaining:", attempts)

print("Thanks for playing Hangman!")