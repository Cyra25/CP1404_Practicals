def main():
    name = get_name()
    num = get_frequency()

    for i in range(0, len(name), num):
        print(name[i])


def get_frequency():
    num = input("What is the frequency of the letter?")
    while not num.isdigit() == False:
        print("Invalid, not digit")
        num = input("What is the frequency of the letter?")

    num = int(num)
    return num


def get_name():
    name = input("your name?")
    while len(name) < 1:
        print("Invalid")
        name = input("your name?")
    return name


main()