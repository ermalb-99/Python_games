import random
from random import randint

print(f"Welcom To The Numer Guess Game !! 🕹️😈😈 \n")
print(f"Guess a Number from 1 - 100  \n")
hard = 10
easy = 20
difficulty = input(f"Choose a difficulty level [easy 🐓] or [hard 😈] \n")
if difficulty.lower() != "e" or difficulty.lower() != "easy":
    print(f"only E or EASY")
elif difficulty.lower() != "h" or difficulty.lower() != "hard":
    print(f"only H or HARD")
on = True
attemps = 0
num = randint(1, 100)
while on:

    if difficulty.lower() == "easy" or difficulty.lower() == "e":
        attemps = easy
        guess = int(input(f"Guess a num !? \n"))
    elif difficulty.lower() == "hard" or difficulty.lower() == "h":
        attemps = hard

        guess = int(input(f"Guess a num !? \n"))
        if guess != int:
            print(f"Only numbers allowed be careful !!")

    if guess == num:
        print(f"Godd Job You Win 🎯!!")
        again = input("Wanna play again ? 😈 🕹️ \n")
        if again.lower() == "yes" or again.lower() == "y":
            num = random.randint(1, 100)
            continue
        else:
            break

    elif guess > num:
        print(f"Too high , higher than {guess} !")
        attemps = attemps - 1
    elif guess < num:
        print(f"Too low , lower than {guess} !")
        attemps = attemps - 1
    elif attemps == 0:
        break
