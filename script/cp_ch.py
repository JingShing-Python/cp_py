import random

def read_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = [name.strip() for name in file.readlines()]
    return names

names_A = read_names('A.txt')
names_B = read_names('B.txt')

name_A = random.choice(names_A)
name_B = random.choice(names_B)

print(f"{name_A}和{name_B}組CP")
