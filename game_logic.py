from curses.ascii import isalpha

from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def is_word_found(word, answer):
    unique_letters_in_secret_word = sorted(set(word))
    unique_letters_in_answer = sorted(set(answer))
    if unique_letters_in_secret_word == unique_letters_in_answer:
        return True
    return False


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
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
        else:
            mistakes += 1
        print("You guessed:", guess)
    if mistakes == 4:
        display_game_state(mistakes, secret_word, guessed_letters)
        print("Game Over, your snowman melted!")
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == "y":
        print("\n")
        play_game()
