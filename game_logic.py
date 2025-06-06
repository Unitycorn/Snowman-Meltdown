from curses.ascii import isalpha
from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def is_word_found(word, answer):
    """
    Makes two sets of characters and compares them. If they are
    equal, the word was found and the game ends
    """
    unique_letters_in_secret_word = sorted(set(word))
    unique_letters_in_answer = sorted(set(answer))
    if unique_letters_in_secret_word == unique_letters_in_answer:
        return True
    return False


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the snowman stage for the current number of mistakes.
    Also displays a partial version of the secret word, depending on
    how many letters were found
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """
    The main logic. If the word was found, the game ends.
    Otherwise, the game continues until 4 mistakes were made.
    Printing appropriate messages if won or lost and asking to play again.
    ALso checks user input for a single, alphabetical character
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    while mistakes < 4:
        if is_word_found(secret_word, guessed_letters):
            print(f"\nYou guessed the word '{secret_word}', congratulations!")
            break
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not isalpha(guess):
            print("\nERROR: Invalid input.")
            continue
        if guess in secret_word and guess not in guessed_letters:
            guessed_letters.append(guess)
            print("\nYou guessed correct:", guess)
        else:
            mistakes += 1
            print("\nYour guess was wrong:", guess)
    if mistakes == 4:
        display_game_state(mistakes, secret_word, guessed_letters)
        print("Game Over, your snowman melted!")
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == "y":
        print("\n")
        play_game()
