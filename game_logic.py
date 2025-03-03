# Imports
import random

# List of Genres with words related
words = {
    "Anime": ['Bleach', 'Naruto', 'One Piece', 'Attack on Titan', 'Death Note', 'Fullmetal Alchemist', 'Jujutsu Kaisen', 'Demon Slayer'],
    "Car Brands": ['Nissan', 'Puma', 'Volkswagen', 'Toyota', 'Ford', 'Chevrolet', 'BMW', 'Mercedes-Benz', 'Audi'],
    "Movies": ['Oppenheimer', 'Barbie', 'Dune', 'Star Wars', 'Inception', 'Interstellar', 'The Matrix', 'The Dark Knight', 'Parasite'],
    "Series": ['Peaky Blinders', 'Game of Thrones', 'Suits', 'Breaking Bad', 'Stranger Things', 'The Witcher', 'Sherlock', 'Black Mirror'],
    "Fruits": ['Banana', 'Apple', 'Watermelon', 'Mango', 'Pineapple', 'Grapes', 'Strawberry', 'Blueberry', 'Cherry']
}


# Choose Difficulty
def difficulty_guesses():
    print ("__ CHOOSE THE DIFFICULTY OF THE GAME __")
    print ("1    -->     EASY [09 GUESSES]\n2    -->     MEDIUM [06 GUESSES]\n3    -->     HARD [3 GUESSES]\n")

    game_difficulty = {"1": 9, "2": 6, "3": 3}  # guesses

    # Validate
    while True:
        user_difficulty = input("Your choice:   ")
        if user_difficulty not in game_difficulty:
            print ("Invalid Choice! Just numbers 1, 2 or 3.")  # invalid
        else:
            return game_difficulty[user_difficulty]  # valid


# Choose Category
def category_word():
    print ("__ CHOOSE THE SUBJECT OF THE WORDS __")
    print (list(words.keys()))

    # Validate
    while True:
        user_category = input("Your choice:   ").title()
        if user_category not in words.keys():
            print ("Invalid Category! Try again.")  # invalid
        else:
            break  # valid

    game_random_word = random.choice(words[user_category])  # Get random word inside the subject
    game_encrypted_word = ["_" if char.isalpha() else char for char in game_random_word]

    return game_random_word, game_encrypted_word


# Update Encrypted Word
def update_encrypted_word(word, encrypted_word, guessed_letter):
    for i in range(len(word)):
        if word[i].upper() == guessed_letter.upper():
            encrypted_word[i] = word[i]  # Reveal the letter

    return encrypted_word  # Return the updated encrypted word as a list


# Main game
def play_hangman():
    attempts = difficulty_guesses()
    word, encrypted_word = category_word()
    guessed_letters = []

    while attempts > 0:
        print("\nCurrent word:", " ".join(encrypted_word))  # Displaying spaces correctly
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        print("Incorrect guesses remaining:", attempts)

        # Check if the word has been completely guessed
        if "_" not in encrypted_word:
            print("\nCongratulations! You guessed the word:", word)
            return encrypted_word, guessed_letters, attempts  # Game over after guessing correctly

        guess = input("Guess a letter: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # Prevent repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word.upper():
            print(f"Good job! '{guess}' is in the word.")
            encrypted_word[:] = update_encrypted_word(word, encrypted_word, guess)  # Update in place
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

        # At the end of the game, correctly print the final word format
        print("\nGame Over! The word was:", word)
        print("Final word progress:", " ".join(encrypted_word))  # Ensure it's displayed correctly

    return encrypted_word, guessed_letters, attempts  # Return values even if game ends

# __ NOTEPAD __
# The choice() method returns a randomly selected element from the specified sequence.: https://www.w3schools.com/python/ref_random_choice.asp
# The join() method takes all items in an iterable and joins them into one string.: https://www.w3schools.com/python/ref_string_join.asp