# num_months = int(input("How many months?"))
#
#
# incomes = []
# total = 0
# for i in range(1,num_months+1):
#     income_per = input("Enter income for month {}: ".format(i))
#     income_per = int(income_per)
#     incomes.append(income_per)
#     total += income_per
# print("Income Report")
# print("--------------")
# for i in range(1,num_months+1):
#     print("Month {} - Income: $ {} Total: $ {}".format(i, incomes, total))

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
