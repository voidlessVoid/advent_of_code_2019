import operator


def load_input_to_dict(path):
    content = {}
    with open(path) as file:
        for i, line in enumerate(file):
            content[i] = line.split(",")
    return content


def conversion(content, cable, count_steps=False):
    cable_position = [0, 0]
    cable_path = content[cable]
    cable_path_convert = []

    directions = {"R": (0, operator.add, "-"),
                  "L": (0, operator.sub, "-"),
                  "U": (1, operator.add, "|"),
                  "D": (1, operator.sub, "|"),
                  }
    counter = 0
    for move in cable_path:
        axis = directions[move[0:1]][0]
        op = directions[move[0:1]][1]
        pos = cable_position[axis]

        if not count_steps:
            for n in range(int(move[1:]) + 1)[1:]:
                cable_position[axis] = op(pos, n)
                cable_path_convert.append(tuple(cable_position.copy()))
        if count_steps:
            for n in range(int(move[1:]) + 1)[1:]:
                counter += 1
                cable_position[axis] = op(pos, n)
                cable_path_convert.append(tuple([counter, *cable_position.copy()]))
                print(counter)
    return cable_path_convert


def distance(p1, p2):
    return (abs(p1[0] - p2[0])) + (abs(p1[1] - p2[1]))


def solution_part1():
    content = load_input_to_dict("input.txt")
    intersections = list(set(conversion(content=content, cable=0)).intersection(set(conversion(content=content, cable=1))))
    ursprung = (0, 0)
    result = []
    for point in intersections:
        result.append(distance(ursprung, point))
    print(f"The smallest distance between intersection point and the main port is: {min(result)}")


def solution_part2():
    content = load_input_to_dict("input.txt")
    intersections = list(set(conversion(content=content, cable=0)).intersection(set(conversion(content=content, cable=1))))

    def counter(dic, data):
        for value in data:
            if value[1:] in intersections:
                dic[value[1:]] = value[0]
        return dic

    cable_a = counter({}, conversion(content=content, cable=0, count_steps=True))
    cable_b = counter({}, conversion(content=content, cable=1, count_steps=True))

    result = []
    for key, value in cable_a.items():
        result.append(cable_b[key] + value)
        print(f"for intersection {key}, the distance is {cable_b[key] + value}")
    print(cable_a)
    print(cable_b)

    print(f"The smalles step number to reach an intersection is: {min(result)}")


# solution_part1()
# right answer 768

solution_part2()
# correct answer: 8684
