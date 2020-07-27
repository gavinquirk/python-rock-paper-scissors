import random

# Possible choices
choices = ["rock", "paper", "scissors"]

# Get user name
user = input('Enter your name: ')
print('Hello ' + user)

# Open ratings file
rating_txt = open('rating.txt', 'r')
rating_list = rating_txt.read().splitlines()

# Convert ratings into dictionary
rating_dict = {}

for entry in rating_list:
    user = entry.split(' ')[0]
    score = int(entry.split(' ')[1])
    rating_dict.update({user: score})


while True:
    # Choices for this round
    computer_choice = random.choice(choices)
    user_input = input("Enter your choice: ")

    # Outputs
    win_output = f"Well done. Computer chose {computer_choice} and failed"
    lose_output = f"Sorry, but computer chose {computer_choice}"
    tie_output = f"There is a draw ({computer_choice})"

    # Exit condition
    if (
        user_input == "!exit"
    ):
        print("Bye!")
        break
    # Invalid user input
    elif (
        user_input not in choices
    ):
        print("Invalid input")
    # Winning conditions
    elif (
        (user_input == "scissors" and computer_choice == "paper") or
        (user_input == "rock" and computer_choice == "scissors") or
        (user_input == "paper" and computer_choice == "rock")
    ):
        print(win_output)
    # Losing conditions
    elif (
        (user_input == "paper" and computer_choice == "scissors") or
        (user_input == "scissors" and computer_choice == "rock") or
        (user_input == "rock" and computer_choice == "paper")
    ):
        print(lose_output)
    # Tie conditions
    elif (
        (user_input == "paper" and computer_choice == "paper") or
        (user_input == "scissors" and computer_choice == "scissors") or
        (user_input == "rock" and computer_choice == "rock")
    ):
        print(tie_output)
