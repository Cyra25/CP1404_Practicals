def memberwiseAddition():
    list_one = [1,2,3]
    list_two = [2,3,4]
    sum_index = [sum(num) for num in zip(list_one,list_two)]
    print(sum_index)