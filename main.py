import random
import art
import os

# global variables
one_to_hun = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
              51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# functions


def clear():
    os.system("clear")


def Opening():
    # local variables
    start_correct = False

    print("W E L C O M E  T O  ")
    print(art.logo + "\n")

    while start_correct != True:
        start = input("W O U L D  Y O U  L I K E  T O  P L A Y ? : ")
        if start == "yes" or start == "no":
            start_correct = True
        else:
            print("I N V A L I D  I N P U T : Y E S  O R  N O  O N L Y .")

    if start == "no":
        print("T E R M I N A T E D .")
        exit()
    else:
        NumRunner()


def Lost():
    # local variables
    print("Y O U  H A V E  L O S T . H A  H A  H A  H A . .   .")

    play_again_l = input(
        " W I L L  Y O U  P L A Y  A G A I N ?  Y E S  O R  N O : ")

    if play_again_l == "yes":
        NumRunner()
    elif play_again_l == "no":
        print("G O O D B Y E . ")
        exit()
    else:
        print("I N V A L I D  R E S P O N S E .  E N O U G H  I S  E N O U G H . I M  D O N E  W I T H  Y O U . ")
        exit()


def Won():
    # local variables
    play_again_w = input(
        " W I L L  Y O U  P L A Y  A G A I N ?  Y E S  O R  N O : ")

    if play_again_w == "yes":
        NumRunner()
    elif play_again_w == "no":
        print("G O O D B Y E . ")
        exit()
    else:
        print("I N V A L I D  R E S P O N S E .  E N O U G H  I S  E N O U G H . I M  D O N E  W I T H  Y O U . ")
        exit()


def NumRunner():
    # local variables
    game_num = random.choice(one_to_hun)
    lives = 10
    mode_correct = False
    player_correct = False
    clear()
    print("A I M :  G U E S S  T H E  C O R R E C T  N U M B E R  B E T W E E N  O N E  T O  O N E  H U N D R E D .")
    while mode_correct != True:
        mode = input("M O D E :  E A S Y  O R  H A R D ? : ")
        if mode == "easy" or mode == "hard":
            mode_correct = True
        else:
            print("I N V A L I D  I N P U T :  E A S Y  O R  H A R D  O N L Y .")

    if mode == "hard":
        lives -= 5

    while player_correct == False:
        player_choice = int(
            input("W H A T  N U M B E R  A M  I  T H I N K I N G ? : "))

        if player_choice > game_num:
            print(
                f"T H E  N U M B E R  ' {player_choice} '  I S  T O O  H I G H .  P L E A S E  R E S E L E C T. ")
            lives -= 1
            if lives < 0:
                break
            print(f"Y O U  H A V E ' {lives} '  L I V E S   L E F T .")
        elif player_choice < game_num:
            print(
                f"T H E  N U M B E R  ' {player_choice} '  I S  T O O  L O W .  P L E A S E  R E S E L E C T. ")
            lives -= 1
            if lives < 0:
                break
            print(f"Y O U  H A V E ' {lives} '  L I V E S  L E F T .")
        else:
            print(
                f"T H E  N U M B E R  ' {player_choice} ' I S  C O R R E C T ! I  A M  B E A T E N ! ")
            player_correct = True

    if lives < 0:
        Lost()
    else:
        Won()

    # timeline
Opening()
