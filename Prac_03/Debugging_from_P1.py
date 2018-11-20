"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    result = take_score(score)
    if result == 4:
        print("Invalid score")
    else:
        if result == "1":
            print("Excellent")
        elif result == "2":
            print("Pass")
        else:
            print("Fail")

    print("thanks")

def take_score(score):
    if score < 0 or score > 100:
        result = "4"
    else:
        if score >= 90:
            result = "1"
        elif score >= 50:
            result = "2"
        else:
            result = "3"
    return result

main()