import random
def hangman():
    word=random.choice(["pugger","littlepugger","thor","tiger","jeevan","east","janaseva","akash","lion","eleohant"])
    validletters='abcdefghijklmnopqrstuvxyz'
    turns=10
    guessmade=''
    while len(word)>0:
        main=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+"_"+""
        if main==word:
            print(main)
            print("you win!")
            break
            
        print("guess the word:",main)
        guess=input()

        if guess in validletters:
            guessmade=guessmade+guess
        else:
            print("enter a valid character")
            guess=input()

        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print(" -------- ")
            if turns==8:
                print("8 turns left")
                print(" -------- ")
                print("     o    ")
            if turns==7:
                print("7 turns left")
                print(" -------- ")
                print("     o    ")
                print("     |    ")
            if turns==6:
                print("6 turns left")
                print(" -------- ")
                print("     o    ")
                print("     |    ")
                print("    /     ")
            if turns==5:
                print("5 turns left")
                print(" -------- ")
                print("     o    ")
                print("     |    ")
                print("    / \   ")
            if turns==4:
                print("4 turns left")
                print(" -------- ")
                print("     o/   ")
                print("     |    ")
                print("    / \   ")
            if turns==3:
                print("3 turns left")
                print(" -------- ")
                print("    \o/   ")
                print("     |    ")
                print("    / \   ")
            if turns==2:
                print("2 turns left")
                print(" -------- ")
                print("    \o/|  ")
                print("     |    ")
                print("    / \   ")
            if turns==1:
                print("1 turns left")
                print("last breate countin take care")
                print(" -------- ")
                print("    \o_|/ ")
                print("     |    ")
                print("    / \   ")
            if turns==0:
                print("you loose ")
                print("you let akind man die")
                print(" -------- ")
                print("     o_|  ")
                print("    /|\   ")
                print("    / \   ")
                break


name=input("enter your name")
print("welcome",name)
print("----------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()