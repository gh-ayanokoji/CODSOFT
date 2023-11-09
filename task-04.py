import random

print("Welcome to Rock Paper Scissor\nRules are Simple and you know it\n")
play = 1
while play == 1:
    choices = "rps"
    index = random.randint(0,2)
    compChoice = choices[index]

    humChoice = input("Enter 'r' for Rock 'p' for Paper or 's' for Scissor: ")

    if humChoice == 'r' and compChoice == 'p':
        print("You chose Rock and Computer chose Paper\nYou Lose")

    elif humChoice == 'r' and compChoice == 's':
        print("You chose Rock and Computer chose Scissor\nCongrats you win")

    elif humChoice == 'r' and compChoice == 'r':
        print("You chose Rock and Computer also chose Rock\nIts a tie!")

    elif humChoice == 'p' and compChoice == 'r':
        print("You chose Paper and Computer chose Rock\nCongrats you win")

    elif humChoice == 'p' and compChoice == 's':
        print("You chose Paper and Computer chose Scissor\nYou Lose")

    elif humChoice == 'p' and compChoice == 'p':
        print("You chose Paper and Computer also chose Paper\nIts a tie!")

    elif humChoice == 's' and compChoice == 'r':
        print("You chose Scissor and Computer chose Rock\nYou Lose")

    elif humChoice == 's' and compChoice == 'p':
        print("You chose Scissor and Computer chose Paper\nCongrats you win")

    elif humChoice == 's' and compChoice == 's':
        print("You chose Scissor and Computer also chose Scissor\nIts a tie!")

    else:
        print("Please enter a valid input")

    play = int(input("Enter 1 to Play Again or 0 to Exit: "))
