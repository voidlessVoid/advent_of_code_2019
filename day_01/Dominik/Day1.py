def load_input_to_list(path):
    with open(path) as file:
        content = file.readlines()
    content = [int(x.strip()) for x in content]
    return content


def fuel_req(mass):
    return mass // 3 - 2


def fuel_req2(mass):
    total_fuel = 0

    def _fuel_req(m):
        fuel = m // 3
        if fuel <= 2:
            return 0
        else:
            return fuel - 2

    fuel_need = _fuel_req(mass)
    if fuel_need > 0:
        total_fuel += fuel_need
        total_fuel += fuel_req2(fuel_need)
    return total_fuel


def solution(path, func):
    summe = 0
    for mass in load_input_to_list(path=path):
        summe += func(mass=mass)
    return summe


"""--- Part One ---"""
# print(solution("input.txt",fuel_req))
"""correct answer: 3275518"""

"""--- Part Two ---"""
print(solution("input.txt", fuel_req2))
"""correct answer: 4910404"""
