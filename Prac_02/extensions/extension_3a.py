"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import string
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
original = input(">>>")
word = ""
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
"""
for kind in original:
    if kind in SPECIAL_CHARACTERS:
        word += random.choice(string.ascii_lowercase)
    else:
        word += kind"""
for kind in original:
    if kind=="#":
        word += random.choice(VOWELS)
    elif kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "*":
        word += random.choice(string.ascii_lowercase)
    else:
        word += kind

print(word,end="")