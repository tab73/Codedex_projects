"""
  Rock Paper Scissors Spock Lizard !

  Create a program where the user plays a round of Rock, Paper, Scissors, Spock, Lizard with the computer.
  The rules are as follows:
    - Scissors cut Paper.
    - Paper covers Rock.
    - Rock crushes Lizard.
    - Lizard poisons Spock.
    - Spock smashes Scissors.
    - Scissors beat Lizard.
    - Lizard eats Paper.
    - Paper disproves Spock.
    - Spock vaporizes Rock.
    - Rock breaks Scissors.
"""
import random

# declaration of variables
player: str = ""
computer: int = 0
# choices
rock: str = "✊"      # 1
paper: str = "✋"     # 2
scissors: str = "✌"  # 3
spock: str = "🖖"     # 4
lizard: str = "🦎"    # 5
player_choice: str = ""
computer_choice: str = ""

# entries
player = input("===================\nRock Paper Scissors\n===================\n1) ✊\n2) ✋\n3) ✌\n4) 🖖\n5) 🦎\nPick a number: ")
computer = random.randint(1, 5)
# entry validity
while not player.isdigit() or int(player) != 1 and int(player) != 2 and int(player) != 3 and int(player) != 4 and int(player) != 5:
    print("Wrong entry ! Please, pick a number between 1 and 3")
    player = input("===================\nRock Paper Scissors\n===================\n1) ✊\n2) ✋\n3) ✌\n4) 🖖\n5) 🦎\nPick a number: ")
player = int(player)

# emoji conversion
if player == 1:
    player_choice = rock
elif player == 2:
    player_choice = paper
elif player == 3:
    player_choice = scissors
elif player == 4:
    player_choice = spock
elif player == 5:
    player_choice = lizard

if computer == 1:
    computer_choice = rock
elif computer == 2:
    computer_choice = paper
elif computer == 3:
    computer_choice = scissors
elif computer == 4:
    computer_choice = spock
elif computer == 5:
    computer_choice = lizard

# print entries
print(f"You chose: {player_choice}")
print(f"CPU chose: {computer_choice}\n")

# who's winning
# Scissors cut Paper
if player_choice == scissors and computer_choice == paper:
    print("You won !")
elif computer_choice == scissors and player_choice == paper:
    print("The computer won !")
# Paper covers Rock
elif player_choice == paper and computer_choice == rock:
    print("You won !")
elif computer_choice == paper and player_choice == rock:
    print("The computer won !")
# Rock crushes Lizard
elif player_choice == rock and computer_choice == lizard:
    print("You won !")
elif computer_choice == rock and player_choice == lizard:
    print("The computer won !")
# Lizard poisons Spock
elif player_choice == lizard and computer_choice == spock:
    print("You won !")
elif computer_choice == lizard and player_choice == spock:
    print("The computer won !")
# Spock smashes Scissors
elif player_choice == spock and computer_choice == scissors:
    print("You won !")
elif computer_choice == spock and player_choice == scissors:
    print("The computer won !")
# Scissors beat Lizard
elif player_choice == scissors and computer_choice == lizard:
    print("You won !")
elif computer_choice == scissors and player_choice == lizard:
    print("The computer won !")
# Lizard eats Paper
elif player_choice == lizard and computer_choice == paper:
    print("You won !")
elif computer_choice == lizard and player_choice == paper:
    print("The computer won !")
# Paper disproves Spock
elif player_choice == paper and computer_choice == spock:
    print("You won !")
elif computer_choice == paper and player_choice == spock:
    print("The computer won !")
# Spock vaporizes Rock
elif player_choice == spock and computer_choice == rock:
    print("You won !")
elif computer_choice == spock and player_choice == rock:
    print("The computer won !")
# Rock breaks Scissors
elif player_choice == rock and computer_choice == scissors:
    print("You won !")
elif computer_choice == rock and player_choice == scissors:
    print("The computer won !")
# Equality
elif player_choice == computer_choice:
    print("It's a tie !")