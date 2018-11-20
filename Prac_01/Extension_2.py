name = input("Enter name: ")
print("(H)ello","\n(G)oodbye","\n(Q)uit")
menu = input()
menu = menu.upper()
while menu != "Q":
    if menu == "H":
        print("Hello", name)
    elif menu == "G":
        print("Goodbye", name)
    else:
        print("Invalid")
    print("(H)ello", "\n(G)oodbye", "\n(Q)uit")
    menu = input()
    menu = menu.upper()
print("Finished")