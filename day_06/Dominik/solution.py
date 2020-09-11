def read_input_to_list(path):
    with open(path, "r") as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


class planet():
    def __init__(self, name):
        self.name = name
        self.satellites = []
        self.orbits_around = None

    def add_satellite(self, name):
        self.satellites.append(name)

    def add_orbit(self, name):
        self.__setattr__("orbits_around", name)


def navigate(planet, path: list, nr=0, ):
    while not planet.orbits_around is None:
        path.append(planet.orbits_around.name)
        nr += 1
        center = navigate(planet.orbits_around, path, nr)
        return center
    return path, nr


def part_a():
    count = 0
    for path in system_dict.keys():
        count += navigate(system_dict[path], [])[1]
    print(count)


def part_b():
    you_path = navigate(system_dict["YOU"], [])[0]
    san_path = navigate(system_dict["SAN"], [])[0]
    duplets = set(you_path).intersection(set(san_path))
    jump_path = list(set(you_path) - duplets) + list(set(san_path) - duplets)
    print(len(jump_path))


content = read_input_to_list("input.txt")
system_dict = {}
system = [x.split(')') for x in content]

for center, satellite in system:
    if center not in system_dict:
        system_dict[center] = planet(center)
    if satellite not in system_dict:
        system_dict[satellite] = planet(satellite)

for center, satellite in system:
    system_dict[satellite].add_orbit(system_dict[center])
    system_dict[center].add_satellite(system_dict[satellite])

part_a()
### correct answer 387356
part_b()
### correct answer 532
