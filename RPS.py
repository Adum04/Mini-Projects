"""
ROCK PAPER SCISSOR GAME USED 
1.IMPORT MODULE
2.WHILE LOOP
3.CONTINUE AND BREAK STATEMENTS
4.IF-ELSE STATEMENTS
"""

# R= Rock
# P= Paper
# S= Scissors
import random

options = ["R", "P", "S"]
print(options)
while True:
    Your_choice = input("Enter Your Choice: ")
    if Your_choice not in options:
        print("Enter Valid Option")
        continue

    Computer_choice = random.choice(options)
    print(f"Your Choice is {Your_choice}\ncomputer choice is {Computer_choice}")

    if Your_choice == Computer_choice:
        print(f"The Match is tied Both have chosen {Your_choice}")

    elif Your_choice == "R":
        if Computer_choice == "P":
            print("Computer wins")
        elif Computer_choice == "S":
            print("You win")

    elif Your_choice == "P":
        if Computer_choice == "R":
            print("You win")
        elif Computer_choice == "S":
            print("Computer win")

    elif Your_choice == "S":
        if Computer_choice == "R":
            print("Computer win")
        elif Computer_choice == "P":
            print("You win")

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again != "Y":
        break
