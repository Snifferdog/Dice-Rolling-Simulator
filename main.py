import random

def roll():
    side = random.randrange(1, 6)
    if side == 1:
        print("|---|")
        print("|-1-|")
        print("|---|")
    if side == 2:
        print("|---|")
        print("|-2-|")
        print("|---|")
    if side == 3:
        print("|---|")
        print("|-3-|")
        print("|---|")
    if side == 4:
        print("|---|")
        print("|-4-|")
        print("|---|")
    if side == 5:
        print("|---|")
        print("|-5-|")
        print("|---|")
    if side == 6:
        print("|---|")
        print("|-6-|")
        print("|---|")

def startup():
    print("Welcome to Dice Simulator 2015!")
    raw_input("Press enter to roll...")
    roll()

startup()



