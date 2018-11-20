name = input("your name?")
while len(name)< 1:
    print("Invalid")
for i in range(0,len(name),2):
    print(i)