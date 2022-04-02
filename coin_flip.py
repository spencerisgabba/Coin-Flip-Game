from ast import While
import sys
import random

def coinflip(n):
    """
    Takes n input, resets coin count, then iterates through n times. Generates
    random integer between 1 and 0, 1 is heads and 0 is tails. Adds random to count
    based upon result
    """
    heads = 0
    tails = 0
    for i in range(n):
        flip = random.randint(0,1)
        if flip == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails

print("""
 _  _  ____   __   ____  ____     __  ____    ____  __   __  __    ____ 
/ )( \(  __) / _\ (    \/ ___)   /  \(  _ \  (_  _)/ _\ (  )(  )  / ___)
) __ ( ) _) /    \ ) D (\___ \  (  O ))   /    )( /    \ )( / (_/  ___ 
\_)(_/(____)\_/\_/(____/(____/   \__/(__\_)   (__)\_/\_/(__)\____/(____/

By Spencer Schmidt [spennccee.schmidt0@gmail.com]

""")
# Code below is mainy input validation
while True:
    print("P to Play Q to Quit\n")
    init = input("> ")
    if init.upper() == "Q":
        sys.exit()
    if init.upper() == "P":
        break
    print("\nPlease enter a valid option.\n")
while True:
    n = int(input("\nEnter a positive integer\n\n> "))
    if n >= 1:
        if n >= 500000:
            print("\nThis may take a while...")
        heads, tails = coinflip(n)
        print(f"\n{heads}: Heads\n{tails}: Tails")
        while True:
            continue_game = input("\nPlay again? Y or N\n> ")
            if continue_game.upper() == "Y":
                break
            if continue_game.upper() == "N":
                sys.exit()
    else:
        print("\nERROR: Enter a valid integer.")