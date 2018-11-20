"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
import random
import string

password = ""
MIN_LENGTH = int(input("please enter the minimum length of the password"))
MAX_LENGTH = int(input("Please enter the maximum length of the password"))
SPECIAL_CHARS_REQUIRED = input("Is special characters required?:True or False")

UPPER_REQUIRED = input("Is uppercase letter required?:True or False").lower()


SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

digit_required = input("Is digit required?:True or False")
digit_required = digit_required.lower()
"""
while digit_required != "true" or digit_required != "false":
    digit_required = input("Is digit required?:True or False")
    digit_required = digit_required.lower()"""

if digit_required == "true":
    password += random.choice(string.digits)
    print(password)
else:
    pass

if upper_required == "true":
    password += random.choice(string.ascii_uppercase)
    print(password)
else:
    pass

if special_chars_required == "true";
    pass



"""
def main():

    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):

    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1

        if char.islower():
            count_lower +=1

        if char.isupper():
            count_upper +=1
        if char in SPECIAL_CHARACTERS:
            count_special += 1
    if (count_upper == 0 or count_lower==0 or count_digit==0):
        return False

    # for char in password:

    if count_special == 0:
        return False
    return True
main()
"""