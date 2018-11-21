import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def main():
    word_format = input(">>>>>").lower()
    valid_not = is_valid(word_format)
    while valid_not is False:
        word_format = input(">>>").lower()
        valid_not = is_valid(word_format)
    password = create_pass(word_format)
    print(password)

def create_pass(word_format):
    password = ""
    for kind in word_format:
        if kind == "c":
            password += random.choice(CONSONANTS)
        else:
            password += random.choice(VOWELS)
    return password

def is_valid(word_format):
    for char in word_format:
        if not (char == "c" or char == "v"):
            valid_not = False
        elif char == "c" or char == "v":
            valid_not = True
    return valid_not
main()