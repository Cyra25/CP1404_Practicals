def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    score_subject = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")#lists but in string
        score_numbers = [int(value) for value in score_strings] #make it all integer
        score_values.append(score_numbers) #list inside the list
    scores_file.close()
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        score_subject.append([]) #empty list for nested list
        for n in range(len(scores_data)-1):
            print(score_values[n][i])
            score_subject[i].append(score_values[n][i])

        print("Min:", min(score_subject[i]))
        print("Average", sum(score_subject[i])//len(scores_data)-1)#average of each subject inside subjects



main()