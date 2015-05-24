import random

def roll():
    side = random.randrange(1, 6)
    return side

def startup():
    print("Welcome to Dice Simulator 2015!")
    raw_input("Press enter to roll...")
    print(roll())

startup()



