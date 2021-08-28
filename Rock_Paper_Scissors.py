from random import randint

#Create a list of  Pla Options

t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer

computer = t[randint(0,2)]

#set player to false

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Yes lose!", computer, "covers", player)
        else:
            print("Yes win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("Yes lose!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Yes lose!", computer, "smashes", player)
        else:
            print("Yes lose!", player, "cuts", computer)
    else:
        print("Thats not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]
