import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(f"Welcome to the RPS !")

game = True
while game:
    user_joice = int(input(f"Type 1 for ROCK , 2 for PAPER and 3 for SCISSORS \n"))
    if user_joice > 3:
        print(f"YOU PUT INVALID NUMBER ONLY 3")
    comp_joice = random.randint(1, 3)

    if user_joice == 1 and comp_joice == 1:
        print(f"{rock} {rock}")
        print("EVEN !")
    elif user_joice == 2 and comp_joice == 2:
        print(f"{paper} {paper}")
        print("EVEN !")
    elif user_joice == 3 and comp_joice == 3:
        print(f"{scissors} {scissors}")
        print("EVEN !")
        """USER WINS"""
    elif user_joice == 1 and comp_joice == 3:
        print(f"{rock} {scissors}")
        print("YOU WIN !")
    elif user_joice == 2 and comp_joice == 1:
        print(f"{paper} {rock}")
        print("YOU WIN !")
    elif user_joice == 3 and comp_joice == 2:
        print(f"{scissors} {paper}")
        print("YOU WIN !")
        """COMP WINS"""
    elif user_joice == 3 and comp_joice == 1:
        print(f"{scissors} {rock}")
        print("YOU LOSE !")
    elif user_joice == 1 and comp_joice == 2:
        print(f"{rock} {paper}")
        print("YOU LOSE !")
    elif user_joice == 2 and comp_joice == 3:
        print(f"{paper} {scissors}")
        print("YOU LOSE !")
    else:
        print(f"INCORRET NUMBER ONLY 1 , 2 ,3")
    game_again = input(f"Wanna Play Again ? \n")
    if game_again.lower() == "yes" or game_again.lower()=="y":
        continue
    else:
        break


