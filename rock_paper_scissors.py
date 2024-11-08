import random

print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]

def computer_pick():
    return random.choice(choices)

def user_pick():
    while True:
        user_choice = input("Please enter a value between (1 and 3) Rock[1], Paper[2], Scissors[3]: ")
        if user_choice in ["1", "2", "3"]:
            return choices[int(user_choice) - 1]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

user_score = 0
computer_score = 0

def print_score():
    print(f"User: {user_score} | Computer: {computer_score}")

def win():
    global user_score 
    user_score += 1
    print("You win!")
    print_score()

def lose():
    global computer_score
    computer_score += 1
    print("You lose!")
    print_score()

def who_wins(computer, user):
    print(f"Computer picked {computer}, you picked {user}.")
    if computer == user:
        print("It's a draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        win()
    else:
        lose()

def start():
    while True:
        computer_choice = computer_pick()
        user_choice = user_pick()
        who_wins(computer_choice, user_choice)

        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == "n":
                print("Thank you for playing!")
                print_score()
                return
            elif play_again == "y":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# Start the game
start()