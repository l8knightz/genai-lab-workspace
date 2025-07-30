# Hangman Game - Day 7 of 100 Days of Python

import random

# Establish a list of words that can be chosen for the game
with open("words.txt") as f:
    word_list = f.read().splitlines()
# Randomly select a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)  # For debugging purposes, to see the chosen word
for letter in chosen_word:
    print("_", end=" ")  # Print underscores for each letter in the chosen word
print()

print("Welcome to Hangman!")
print(r'''   |/|
   | |
   |/|
   | |
   |/|
  (___)
  (___)
  (___)
  (___)
  (___)
  // \\
 //   \\
||     ||
||     ||
||     ||
 \\___//
  -----''')
print()
print("Guess the word by entering one letter at a time. \nYou have 6 incorrect guesses before you lose.")
print("Let's start the game!")
print("\nThe word has", len(chosen_word), "letters.\n")
for letter in chosen_word:
    print("_", end=" ")  # Print underscores for each letter in the chosen word
print()
game_over = False
correct_letters = []  # List to keep track of correctly guessed letters
incorrect_letters = []  # List to keep track of incorrectly guessed letters
hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stage = 0  # Initialize the stage of the hangman

# Begin the game loop
while not game_over:
    guessed_word = ""  # Reset the guessed letters for each new guess
    picked = input("Guess a letter: ").lower()  # Ask the user to guess a letterh
    for letter in chosen_word:
        if letter == picked or letter in correct_letters:
            guessed_word += letter + " "  # Print the letter if it matches the guess
            correct_letters.append(picked)  # Add the letter to correct guesses
        else:
            guessed_word += "_ "
    print()
    print(guessed_word.strip())  # Print the current state of guessed word

    if "_" not in guessed_word:
        # If there are no underscores left, the user has guessed the word
        print("You win!")
        game_over = True
    else:
        print("\nTry again!")
    if picked not in chosen_word and picked not in incorrect_letters:
        # If the guessed letter is not in the word and hasn't been guessed before
        incorrect_letters.append(picked)
        print(f"Incorrect guesses: {', '.join(incorrect_letters)}")  # Show incorrect guesses
        stage += 1 
        if stage >= len(hangman_stages):
            # If the user has reached the maximum number of incorrect guesses
            print("You lose! The word was:", chosen_word)
            game_over = True
    elif picked in incorrect_letters:
        # If the letter has already been guessed incorrectly
        print(f"You already guessed '{picked}' incorrectly. Try another letter.")

    print(hangman_stages[stage])  # Print the current hangman stage
