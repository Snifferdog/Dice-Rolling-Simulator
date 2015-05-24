import random

def roll():
    return random.randrange(1, 6)

def startup():
    print("Welcome to Dice Simulator 2015!")
    raw_input("Press enter to roll...")
    print(roll())

startup()



