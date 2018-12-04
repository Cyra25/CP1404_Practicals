string_list = []
string_inp = "empty"
while not string_inp == "":
    string_inp = input(">>>")
    if string_inp != "":
        string_list.append(string_inp)
repeat = []
for n in range(len(string_list)):
    if string_list.count(string_list[n]) > 1:
        repeat.append(string_list[n])
if repeat == []:
    print("No repeated strings")
else:
    repeat(dict.fromkeys(repeat))
    print("Repeated strings:", ', '.join(repeat))