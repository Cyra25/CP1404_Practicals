character = input("Enter a character: ")
new_num = ord(character)
print("The ASCII for ",character,"is ",new_num)

number = int(input("Enter a number between 33 and 127: "))
while number < 33 or number > 127:
    print("Invalid")
    number = int(input("Enter a number between 33 and 127: "))
new_chr = chr(number)
print(new_chr)
column = input("How many columns do you want to print?")

for i in range(33, 128):
    ch = chr(i);
    print("{:>4}".format(i),"{:>4}".format(ch))

