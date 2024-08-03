import random

user_wins = 0 
computer_wins = 0

def user_choice():
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            quit()
        elif user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Please type Rock/Paper/Scissors or Q to quit")

def computer_choice():
    random_choice = random.randint(0, 2)
    if random_choice == 0:
        return "rock"
    elif random_choice == 1:
        return "paper"
    else:
        return "scissors"

def compare(user_choice, computer_choice):
    global user_wins
    global computer_wins
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("Draw!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

while True:
    user_input = user_choice()
    computer_input = computer_choice()
    compare(user_input, computer_input)
    print(f"You won {user_wins} times and the computer won {computer_wins} times")
