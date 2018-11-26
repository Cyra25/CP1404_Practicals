number_list = []
for i in range(0,5):
    number = int(input("Number: "))
    number_list.append(number)

print("The first number is {}\nThe last number is {}\n".format(number_list[0], number_list[-1]))
print("The smallest number is {}\nThe largest number is {}".format(min(number_list),max(number_list)))
print("The average of numbers is {}".format(sum(number_list)/len(number_list)))