import random

print('Rock Paper Scissor')

game = ["rock", "paper", "scissor"]

user = 0
computer = 0

while True:
    user_type = input("Type rock/paper/scissor or exit : ").lower()

    if user_type == "exit":
        quit()

    if user_type not in game:
        continue

    randomnumber = random.randint(0, 2)
    computer_type = game[randomnumber]

    print("Computer \t\t\t\t\t\t: " + computer_type)

    if user_type == "rock" and computer_type == "scissor":
        print("You won")
        user = user + 1
    elif user_type == "scissor" and computer_type == "paper":
        print("you won")
        user = user + 1
    elif user_type == "paper" and computer_type == "rock":
        print("You won")
        user = user + 1
    elif user_type == computer_type:
        print("Match Draw")
    else:
        print("Computer won")
        computer = computer + 1

    print("Your Score     : ", user)
    print("Computer Score :", computer,"\n")
