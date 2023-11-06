def add(todo):
    with open("todo.txt", "a") as f:
        f.write(f"{todo}")
        f.write("\n")
        print(f"\nYour todo : {todo} - has been successfully added")

def display(lines):
    with open("todo.txt", "r") as f:
            print("\nYour todo list is: ")
            for i in range(lines):
                line = f.readline()
                print(f"{i+1}.{line}", end="")
            print()

def update(lines):
    display(lines)
    upd = input("Type in the todo you want to update(without no.):\n ")
    newTodo = input("What do you want to update with: ")
    with open("todo.txt", "r+") as f:
        data = f.read()
        if upd not in data:
            print("you did a mistake or todo is ot available")
        else:
            data = data.replace(upd, newTodo)
        with open("todo.txt", "w") as f:
            f.write(data)
    print("\nYour list has been updated!\nNew list: ")
    display(lines)
        
def mark(lines):
    display(lines)
    upd = input("Type in the todo you want to mark(without no.):\n ")
    with open("todo.txt", "r+") as f:
        data = f.read()
        if upd not in data:
            print("you did a mistake or todo is ot available")
        else:
            data = data.replace(upd, f"{upd} - Done")
        with open("todo.txt", "w") as f:
            f.write(data)
    print(f"\n{upd} has been marked Done!\nNew list: ")
    display(lines)

def clear():
    with open("todo.txt","w") as f:
        f.write("")

count = 0
run = 1
while run != 0:
    print("1.Add a Todo\n2.Display all Todos\n3.Mark a Todo\n4.Update a Todo\n5.Clear the todo list\n0.Quit")
    temp = int(input("\nWhat do you want to do: "))

    if temp == 1:
        adds = 1
        while adds == 1:
            todo = input("\nEnter your todo: ")
            add(todo)
            count+=1
            adds = int(input("\nEnter 1 to add another todo or 0 to exit: "))

    elif temp == 2:
        display(count)

    elif temp == 3:
        mark(count)

    elif temp == 4:
        update(count)

    elif temp == 5:
        clear()
        count = 0
        print("\nYour todo list has been cleared\n")

    elif temp == 0:
        run = 0

