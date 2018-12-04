number_list = []
num = 0
i = 0
while not num < 0:
    print("Number ",i+1)
    num = int(input())
    i += 1
    number_list.append(num)
del number_list[-1]
print("The first number is {}\nThe last number is {}\n".format(number_list[0], number_list[-1]))
print("The smallest number is {}\nThe largest number is {}".format(min(number_list),max(number_list)))
print("The average of numbers is {}".format(sum(number_list)/len(number_list)))