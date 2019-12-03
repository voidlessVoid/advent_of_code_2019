import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    DIRS = {"L":1j,"R":-1j,"U": -1,"D":1}
    wire_1, wire_2 = read_input_lines()

    def dir_list_to_set(dir_list):
        s = set()
        loc = 0
        for instruction in dir_list:
            dir = instruction[0]
            steps = int(instruction[1:])
            for step in range(steps):
                loc += DIRS[dir]
                s.add(loc)
        return s

    wire_1_set = dir_list_to_set(wire_1.split(','))
    wire_2_set = dir_list_to_set(wire_2.split(','))
    crossings = wire_1_set & wire_2_set
    min_dist = min(x.real + x.imag for x in crossings )
    print(min_dist)


part_a()
def part_b():
    DIRS = {"L": 1j, "R": -1j, "U": -1, "D": 1}
    wire_1, wire_2 = read_input_lines()

    def dir_list_to_dict(dir_list):
        d = {}
        loc = 0
        i=0
        for instruction in dir_list:
            dir = instruction[0]
            steps = int(instruction[1:])
            for step in range(steps):
                loc += DIRS[dir]
                i+=1
                if not loc in d:
                    d[loc] = i
        return d

    wire_1_set = dir_list_to_dict(wire_1.split(','))
    wire_2_set = dir_list_to_dict(wire_2.split(','))
    crossings = set(wire_1_set) & set(wire_2_set)
    min_dist = min(wire_1_set[x]+wire_2_set[x] for x in crossings)
    print(min_dist)

part_b()