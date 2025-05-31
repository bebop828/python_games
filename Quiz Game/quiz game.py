import random
from quiz_game_questions import questions  

def run_quiz(questions):
    score = 0
    for question in questions:         
        print(question["prompt"])
        for option in question["options"]:
            print(option)        
        
        while True:
            answer = input("Enter your answer: ").upper()
            if answer in ['A', 'B', 'C', 'D']:
                if answer == question["answer"]:
                    print("That's correct. Please continue.\n")
                    score += 1 
                else:
                    print("Sorry, that is not correct. The answer is", question["answer"], "\n")
                break  
            else:
                print("Sorry, that is an incorrect input. Please enter A, B, C, or D.") 
                

    return score

def main():
    print("Are you ready to test your knowledge on general trivia?")
    print("Here are 5 questions for you to answer. Good Luck!")
    while True:
        start_game = input("Care to give the quiz game a try? (Y/N): ").lower()
        if start_game == 'y':
            break  
        elif start_game == 'n':
            print("OK! Maybe next time. Goodbye!")
            return  
        else:
            print("Invalid input. Please enter Y for yes or N for no.")
            

    while True:
        selected_questions = random.sample(questions, 5)  
        score = run_quiz(selected_questions)

        print(f"You got {score} out of {len(selected_questions)} questions correct.")
        print("Never stop learning!!!")
        
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