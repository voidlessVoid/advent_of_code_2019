import os
import numpy as np
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
    map = read_input_lines()
    coords = {(i,j) for i in range(len(map)) for j in range(len(map[i]))}
    coords = {(i,j) for i, j in coords if map[i][j]=='#'}

    best = 0
    for coord_a in coords:
        dir_set = set()
        for coord_b in coords - {coord_a}:
            dy = coord_a[1] - coord_b[1]
            dx = coord_a[0] - coord_b[0]
            try:
                dydx = dy/dx
            except ZeroDivisionError:
                dydx = np.sign(dy) * float('inf')
            dir_set.add((dydx,np.sign(dx)))
        best = max([len(dir_set), best])
    print(best)

part_a()

def part_b():
    center = (25, 22)
    map = read_input_lines()
    coords = {(i,j) for i in range(len(map)) for j in range(len(map[i]))}
    coords = {(i,j) for i, j in coords if map[i][j] == '#'}

    astroid_dir_dict = defaultdict(list)
    for coord in coords - {center}:
        dy = coord[0] - center[0]
        dx = coord[1] - center[1]
        try:
            dydx = dy / dx
        except ZeroDivisionError:
            dydx = np.sign(dy) * float('inf')

        astroid_dir_dict[(-np.sign(dx) or -1,dydx)].append(coord)

    for dir in astroid_dir_dict:
        astroid_dir_dict[dir] = sorted(astroid_dir_dict[dir], key = lambda x: (x[1] - center[1])**2 + (x[0]-center[0])**2 , reverse=True)

    sorted_dirs = sorted(astroid_dir_dict.keys())
    sorted_dirs_queue = deque(sorted_dirs)
    for i in range(200):
        next_dir = sorted_dirs_queue.popleft()
        next_astroid = astroid_dir_dict[next_dir].pop()
        if astroid_dir_dict[next_dir]:
            sorted_dirs_queue.append(next_dir)

    print(100 *next_astroid[1]  + next_astroid[0])

part_b()