"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number"))
        finished = True
        #this is true only when it does no fall under exception
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)