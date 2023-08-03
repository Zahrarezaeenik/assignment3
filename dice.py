import random
def Dice():
    Start=int(input(" 1.Roll the dice \n 2.Exit \n Enter:"))
    if Start!=1:
        return

    roll=random.randint(1,6)
    if(roll==6):
        print(" your number is 6 , you can roll the dice again.")
        Dice()
    else:
        print(f" your number is {roll}")
    
Dice()