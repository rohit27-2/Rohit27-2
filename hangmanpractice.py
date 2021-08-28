import random

def hangman():
    #predefined list
    word = random.choice(["avengers" ,"hulk" , "superman" , "batman" , "ironman" , "captain america" , "thor" , "falcon"])
    chances = 10
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    guessmade = ''

    while len(word) > 0 :
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else :
                main = main + "_" + " "
            
        if main == word:
            print(main)
            print("You Win!")
            break

        print("Guess The Word:  ", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            chances = chances - 1
            if  chances == 9 :
                print("9 turns left")
                print("===========")
            if  chances == 8:
                print("8 turns left")
                print("===========")
                print("     0     ")
            if chances == 7:
                print("7 turns left")
                print("===========")
                print("     0     ")
                print("     |     ")
            if chances == 6:
                print("6 turns left")
                print("===========")
                print("     0     ")
                print("     |     ")
                print("    /      ")
            if chances == 5:
                print("5 turns left")
                print("===========")
                print("     0     ")
                print("     |     ")
                print("    / \    ")
            if chances == 4:
                print("4 turns left")
                print("===========")
                print("   \ 0     ")
                print("     |     ")
                print("    / \    ")
            if chances == 3:
                print("3 turns left")
                print("===========")
                print("   \ 0 /   ")
                print("     |     ")
                print("    / \    ")
            if chances == 2:
                print("2 turns left")
                print("===========")
                print("   \ 0 /|  ")
                print("     |     ")
                print("    / \    ")
            if chances == 1:
                print("1 turns left")
                print("THis is your last chance")
                print("===========")
                print("   \ 0_ / |")
                print("     |     ")
                print("    / \    ")
            if chances == 0:
                print("You lose")
                print("you let a kibd men die")
                print("===========")
                print("     0_  |")
                print("    /|\   ")
                print("    / \   ")
                break

            





#Interferce
name = input("Enter Your Name Please...: ")
print("=======================")
print("This is a hangman name")
print("=======================")
print(f"Hello {name}")

#this is a function
hangman()
print()