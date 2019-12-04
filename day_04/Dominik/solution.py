#! Python 3.6

input_min = 265275
input_max = 781584


def solution_part1(i_range, printing=False):
    result = []
    for i in range(*i_range, 1):
        value = int("".join(sorted(str(i))))
        if value > i_range[0] and len(set(str(value))) < len(str(value)):
            result.append(value)
    if not printing:
        return sorted(list(set(result)))
    else:
        print(f"Number of passwords matching the criteria: {len(sorted(list(set(result))))}")


# solution_part1((input_min, input_max), printing=True)
# correct answer 960

def solution_part2():
    result = []
    for i in solution_part1((input_min, input_max), printing=False):
        counter = []
        for c in set(str(i)):
            counter.append(str(i).count(c))
        if 2 in counter:
            result.append(i)
    print(f"Number of passwords matching the criteria: {len(result)}")


solution_part2()
# correct answer 626
