def read_input_to_list(path):
    with open(path, "r") as f:
        content = f.readline()
    return [int(x) for x in content.split(",")]


def chunks(lst, n):
    start = 0
    for i in range(0, len(lst), n):
        if lst[start] == 99:
            yield lst[start:start + 1] + (n - 1) * [None]
            start += 1
        else:
            yield lst[start:start + n]
            start += n


def solution_part1(noun: int, verb: int, print_value=True):
    input_list = read_input_to_list("input.txt")
    input_list[1] = noun
    input_list[2] = verb
    array = list(chunks(input_list, 4))

    for chunk in array:
        if chunk[0] == 99:
            break
        elif chunk[0] == 1:
            input_list[chunk[3]] = input_list[chunk[1]] + input_list[chunk[2]]
        elif chunk[0] == 2:
            input_list[chunk[3]] = input_list[chunk[1]] * input_list[chunk[2]]
        array = list(chunks(input_list, 4))

    if print_value:
        return print(f"Searched value is: {input_list[0]}")
    else:
        return input_list[0]


# solution_part1(12,2, print_value=True)
# correct answer: 3716250

def soulution_part2():
    for noun in range(0, 100, 1):
        for verb in range(0, 100, 1):
            result = solution_part1(noun, verb, print_value=False)
            if result == 19690720:
                print(f"Searched value is: 100 * {noun} + {verb} = {100 * noun + verb}")
                break

# correct answer: 100 * 64 + 72 = 6472
