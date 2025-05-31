import random

from hangman_words import words, food, nature, space


print("======================================================")

print("Welcome to HANGMAN!")
print("6 wrong guesses and it's lights out, GAME OVER!!!")
print("Make a game choice selection to begin game play")
print("You will have a selection of games to choose from")
print("Main Game has approx 850 available words")
print("Food with approx 320")
print("Nature with approx 250")
print("Space with approx 320")
print("No sense Hanging Around!!! Let's get to it!")

print("======================================================")


def play_hangman(word_list):
    chosen_word = random.choice(word_list)
    word_display = ['_' for _ in chosen_word]
    guessed_letters = set()

    print("Good Luck")
    print("======================================================")
    print(" ".join(word_display))

    attempts = 6
    incorrect_messages = [
        "Sorry, wrong guess. 5 wrong guesses left before you're done and it's the hangman's rope!",
        "Sorry, that is wrong too. 4 left!",
        "I do hope you are trying. 3 to go. Your half cooked!",
        "Sorry, 2 left! Have you tried the more common letters- E, T, A, O, I",
        "Well, you are at your last wrong guess. No more chances left for a wrong letter. What do you choose?"
    ]

    while attempts > 0 and '_' in word_display:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Sorry, that is not an acceptable choice, please try again.")
            continue

        if guess in guessed_letters:
            print(f"Please select another letter. You have already selected '{guess}'.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = guess
        else:
            attempts -= 1
            if attempts > 0:
                print(incorrect_messages[5 - attempts])
            else:
                print("Sorry, you have run out of guesses and it is GAME OVER!")

        print(" ".join(word_display))

    if '_' not in word_display:
        print("You guessed the word! Congrats")
        print(' '.join(word_display))
        print("You made it out alive!")
    else:
        print("You're DEAD! The word was: " + chosen_word)
        print("WOMP WOMP!")


def main():
    while True:
        print("\nChoose a game option:")
        print("1: Main Game")
        print("2: Food")
        print("3: Nature")
        print("4: Space")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            play_hangman(words)
        elif choice == '2':
            play_hangman(food)
        elif choice == '3':
            play_hangman(nature)
        elif choice == '4':
            play_hangman(space)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        while True:
            replay = input("Would you like to play again? (Y/N): ").lower()
            if replay == 'y':
                break
            elif replay == 'n':
                print("OK! Good-Bye!")
                return
            else:
                print("Invalid input. Please enter Y for yes or N for no.")


if __name__ == "__main__":
    main()