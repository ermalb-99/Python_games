print("Welcome To My Calculator ! \n")
from vizatimi import logo


game = True
print(logo)
while game :
    num1 = int(input("Type in first number !"))
    operator = input("Pick An Operator [ + , - , * , / ] ! \n")
    num2 = int(input("Type in second number ! \n"))
    if operator == "+" or operator == "plus":
        print(f"The result is {num1+num2}")

    elif operator == "-" or operator == "minus":
        print(f"The result is {num1-num2}")
        if num1 > num2:
            print(f"The first number you typed is greater than the second one !")

    elif operator == "*" or operator == "multiply":
        print(f"The result is {num1*num2}")

    elif operator == "/" or operator == "divide":
        print(f"The result is {num1/num2}")
        if num1 < num2 :
            print(f"You cant divide it !")
    again = input("Wanna play again [Y-yes] and [N-no]")
    if again.lower() == "y" or again.lower()=="yes":
        continue
    elif again.lower() == "n" or again.lower()=="no":
        print(f"Calculator shut down !")
        print(f"Thank You")
        break

