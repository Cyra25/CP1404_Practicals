def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def main():
    user_inp = input("enter a string")
    print( word_count(user_inp))

main()