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

    game_difficulty = {"1": 9, "2": 6, "3": 3} # guesses

    # Validate
    while True:
        user_difficulty = input("Your choice:   ")
        if user_difficulty in game_difficulty:
            print ("Invalid Choice! Just numbers 1, 2 or 3.") # invalid
        else:
            return game_difficulty[user_difficulty] # valid


# Choose Category
def category_word():
    print ("__ CHOOSE THE SUBJECT OF THE WORDS __")
    print (list(words.keys()))

    # Validade
    while True:
        user_category = input("Your choice:   ").title()
        if user_category not in words.keys():
            print ("Invalid Category! Try again.") # invalid
        else:
            break # valid

    game_random_word = random.choice(words[user_category])  # Get random word inside the subject
    game_encrypted_word = " ".join("_" for _ in game_random_word)  # Encrypt it

    return game_random_word, game_encrypted_word