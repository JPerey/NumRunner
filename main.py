import random
import art
import os

# global variables


# functions

def opening():
    # local variables
    start_correct = False

    print("W E L C O M E  T O  ")
    print(art.logo + "\n")

    while start_correct != True:
        start = input("W O U L D  Y O U  L I K E  T O  P L A Y ? : ")
        if start == "yes" or start == "no":
            start_correct = True
        else:
            print("I N V A L I D  I N P U T : Y E S  O R  N O  O N L Y")

    if start == "no":
        print("T E R M I N A T E D .")
        exit()
    else:
        NumRunner()


def NumRunner():
    print("wooo")


# timeline

opening()
