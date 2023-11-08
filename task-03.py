import random

run = 1
while run == 1:
    password = ""
    length = int(input("Enter your desired length of password(min - 8): "))

    if length < 8:
        print(f"{length} is a very small length for a password, try a bigger length.")

    else:
        for i in range(length):
            sel = random.randint(1,4)
            if sel == 1:
                item =  "abcdefghijklmnopqrstuvwxyz"
                itemSel = random.randint(0,25)
                password = password + item[itemSel]

            elif sel == 2:
                item = "0123456789"
                itemSel = random.randint(0,9)
                password = password + item[itemSel]

            elif sel == 3:
                item = "@$&_-"
                itemSel = random.randint(0,4)
                password = password + item[itemSel]

            elif sel == 4:
                item =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                itemSel = random.randint(0,25)
                password = password + item[itemSel]

    print(f"Your Password is: {password}")
    run = int(input("Enter 1 to generate another password or 0 to exit: "))



