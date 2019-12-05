import numpy as np

def load_input_to_list(path): ### stolen from domink
    with open(path) as file:
        content = file.readlines()
    content = [int(x.strip()) for x in content]
    return content

module_mass = load_input_to_list('data.txt')

def fuel(mass):
    module_mass = np.floor_divide(mass,3)-2
    if module_mass < 0:
        module_mass = 0
    return module_mass

fuel_mass = []

for i in module_mass:
    fuel_list = [fuel(i)]
    while fuel_list[-1] != 0:
        fuel_list.append(fuel(fuel_list[-1]))
    fuel_mass.append(sum(fuel_list))

print(sum(fuel_mass))
