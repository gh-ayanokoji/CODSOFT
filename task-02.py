run = 1
while run == 1:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n0.Exit")
    opr = int(input("What do you want to do: "))
    if opr == 0: 
        print("Ending Session.....")
        break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if opr == 1:
        print(f"\n{num1} + {num2} = {num1+num2}\n")
    elif opr == 2:
        print(f"\n{num1} - {num2} = {num1-num2}\n")
    elif opr == 3:
        print(f"\n{num1} * {num2} = {num1*num2}\n")
    elif opr == 4:
        print(f"\n{num1} / {num2} = {num1/num2}\n")
    else:
        print("Invalid input please try again")
