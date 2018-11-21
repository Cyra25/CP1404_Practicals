import random
min_born = 10
max_born = 20
min_death = 5
max_death = 25

def main():
    original = 1000
    for i in range(1,11):
        born_percent = random.randint(min_born, max_born)
        born = original * born_percent // 100
        death_percent = random.randint(min_death, max_death)
        death = original * death_percent // 100
        final_pop = original + born - death
        print("\nYear", (i))
        print("*****")
        print(born, "gophers were born.", death, "died.")
        print("Population:",final_pop)

main()