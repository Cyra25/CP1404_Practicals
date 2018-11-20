x = int(input("Enter first number"))
y = int(input("Enter second number"))

print("1) Show the even numbers from ",x, " to ", y)
print("2) Show the odd numbers from ",x, " to ", y)
print("3) Show the squares from ",x, " to ", y)
print("4) Exit the program")
menu = input()

while menu != "4":
    if menu == "1":
        if x % 2 == 0:
            for i in range(x, y+1, 2):
                print(i, end=" ")
                print( )
        elif x % 2 == 1:
            for i in range(x + 1, y+1, 2):
                print(i, end=" ")
                print( )

    elif menu == "2":
        if x % 2 == 1:
            for i in range(x, y+1, 2):
                print(i, end=" ")
                print( )
        elif x % 2 == 0:
            for i in range(x + 1, y+1, 2):
                print(i, end=" ")
                print( )

    elif menu == "3":
        list = (range(x, y+1))
        squared = [ x**2 for x in list]
        print("Squares: " + ",".join(str(x) for x in squared))
    else:
        print("Invalid choice")
    print("1) Show the even numbers from ", x, " to ", y)
    print("2) Show the odd numbers from ", x, " to ", y)
    print("3) Show the squares from ", x, " to ", y)
    print("4) Exit the program")
    menu = input()

