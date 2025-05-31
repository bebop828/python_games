import random

print('Welcome to Higher/Lower!')
print('Try your luck in this old guessing game!')

def guess(x):
    random_number = random.randint(1, x)
    attempt_count = 0

    while True:
        attempt_count += 1 
        try:
            guess = int(input(f'{"Guess a number between 1 and 99:" if attempt_count == 1 else "Guess another number:"} ')) 
        except ValueError:
            print("Invalid input. Please enter a valid number.") 
            continue
        
        if guess < 1 or guess > 99:
            print(f'Attempt {attempt_count}: {guess} is out of the valid range (1-99). Please try again.')
        elif guess < random_number:
            print(f'Attempt {attempt_count}: {guess} is too low. Try a higher number.')
        elif guess > random_number:
            print(f'Attempt {attempt_count}: {guess} is too high. Try a lower number.')
        else:
            print(f'Attempt {attempt_count}: Congrats, you guessed the number correctly: {random_number}')
            break


    print(f'You guessed the number in {attempt_count} attempts!')

    if attempt_count <= 4:
        print("Wow! Look at you. Winner, Winner, chicken dinner!")
    elif attempt_count <= 7:
        print("Um. Good job I guess? You can do better!")
    elif attempt_count <= 9:
        print("At least you can say you figured it out. Finally!")
    else:
        print("Were you even trying?")


def main():
    while True:
        guess(99)
        while True:
            play_again = input("\nWould you like to try again? (y/n): ").strip().lower()
            if play_again == 'n':
                print("Ok! See you another time!!!")
                return
            elif play_again == 'y':
                break
            else:
                print("That is not an acceptable response. Please try again.") 


if __name__ == "__main__":
    main()
