import random

# Possible choices
choices = ["rock", "paper", "scissors"]

# Inputs
user_input = input()
computer_choice = random.choice(choices)

# Outputs
win_output = f"Well done. Computer chose {computer_choice} and failed"
lose_output = f"Sorry, but computer chose {computer_choice}"
tie_output = f"There is a draw ({computer_choice})"

# Winning conditions
if (
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
