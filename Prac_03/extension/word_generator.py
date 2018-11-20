"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("what is the word format?")
word_format=word_format.lower()
word = ""
allowed = set("c" + "v")
while set(word_format) != allowed:
    print("word format is in 'c' and 'v'")
    word_format = input("what is the word format?")

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)