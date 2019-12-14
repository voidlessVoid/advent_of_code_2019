import os
from collections import Counter, ChainMap, defaultdict, deque


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    relations = defaultdict(list)
    for center, orbit in [x.split(')') for x in read_input_lines()]:
        relations[center].append(orbit)

    def update_count(center,ith_orbit):
        count = 0
        for orbit in relations[center]:
            count +=ith_orbit
            count += update_count(orbit, ith_orbit+1)
        return count

    print(update_count('COM',1))

part_a()
def part_b():
    relations = defaultdict(list)
    for center, orbit in [x.split(')') for x in read_input_lines()]:
        relations[center].append(orbit)
        relations[orbit].append(center)

    visitdist = {'YOU' : 0}
    lastvisit = {'YOU',}

    while lastvisit:
        next_lastvisit = set()
        for node_a in lastvisit:
            for node_b in relations[node_a]:
                if node_b not in visitdist:
                    visitdist[node_b] = visitdist[node_a]+1
                    next_lastvisit.add(node_b)
        lastvisit = next_lastvisit


    print(visitdist['SAN'] -2) #2 because transfer from You/SAN to next orbit doesnt count

part_b()
