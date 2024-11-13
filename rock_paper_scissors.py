"""
  Rock Paper Scissors game !

  Create a program where the user plays a round of Rock, Paper, Scissors with the computer.
  The rules are as follows:
    - Rock beats Scissors
    - Scissors beat Paper
    - Paper beats Rock
"""
import random

# declaration of variables
player: str = ""
computer: int = 0
# choices
rock: str = "✊"      # 1
paper: str = "✋"     # 2
scissors: str = "✌"  # 3
player_choice: str = ""
computer_choice: str = ""

# entries
player = input("===================\nRock Paper Scissors\n===================\n1) ✊\n2) ✋\n3) ✌\nPick a number: ")
computer = random.randint(1, 3)
# entry validity
while not player.isdigit() or int(player) != 1 and int(player) != 2 and int(player) != 3:
    print("Wrong entry ! Please, pick a number between 1 and 3")
    player = input("===================\nRock Paper Scissors\n===================\n1) ✊\n2) ✋\n3) ✌\nPick a number: ")
player = int(player)

# emoji conversion
if player == 1:
    player_choice = rock
elif player == 2:
    player_choice = paper
elif player == 3:
    player_choice = scissors

if computer == 1:
    computer_choice = rock
elif computer == 2:
    computer_choice = paper
elif computer == 3:
    computer_choice = scissors

# print entries
print(f"You chose: {player_choice}")
print(f"CPU chose: {computer_choice}\n")

# who's winning
# Rock over Scissors
if player_choice == rock and computer_choice == scissors:
    print("You won !")
elif computer_choice == rock and player_choice == scissors:
    print("The computer won !")
# Scissors over Paper
elif player_choice == scissors and computer_choice == paper:
    print("You won !")
elif computer_choice == scissors and player_choice == paper:
    print("The computer won !")
# Paper over Rock
elif player_choice == paper and computer_choice == rock:
    print("You won !")
elif computer_choice == paper and player_choice == rock:
    print("The computer won !")
# Equality
elif player_choice == computer_choice:
    print("It's a tie !")