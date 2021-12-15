import random

boys = ["Stanley", "Frank", "Samuel", "Victor", "Basil"]
girls = ["Jennifer", "Vision", "Ashley", "Brenda", "Helen"]

names = [boys, girls]


length_names = len(names)
randmom_names = random.randint(0, length_names-1)
names_rand = names[randmom_names]



length_boys = len(boys)

random_boys = random.randint(0, length_boys-1)

randomise = boys[random_boys]

length_girls = len(girls)

random_girls = random.randint(0, length_girls-1)

randomsie_1 = girls[random_girls]

print(f'The one selected for this task is {randomise} and {randomsie_1}')