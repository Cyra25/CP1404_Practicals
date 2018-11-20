def main():
    name = get_name()
    for i in range(0,len(name),2):
        print(i)


def get_name():
    name = input("your name?")
    while len(name) < 1:
        print("Invalid")
        name = input("your name?")
    return name


main()