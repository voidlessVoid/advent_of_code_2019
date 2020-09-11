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
    bugs = set()
    inp = read_input_lines()
    for i in range(5):
        for j in range(5):
            if inp[i][j] == '#':
                bugs.add((i+(1j*j)))

    bughist = set([frozenset(bugs)])

    while True:
        nextbugs = set()
        for i in range(5):
            for j in range(5):
                loc = i+(1j*j)
                count = sum([((loc+dir) in bugs) for dir in [-1,1,1j,-1j]])
                if loc in bugs and count  == 1:
                    nextbugs.add(loc)
                elif (loc not in bugs) and count in (1,2):
                    nextbugs.add(loc)
        frozenbugs = frozenset(nextbugs)
        if frozenbugs in bughist:
            print(sum((2**(x.real*5+x.imag) for x in frozenbugs)))
            return
        bughist.add(frozenbugs)
        bugs = nextbugs


def part_b():
    DIRS = {-1,1,1j,-1j}

    def get_mapping(): # dict loc -> (loc, delta_level)
        def get_inner_interface(dir):
            return (2 + 2j) + dir

        def get_outer_interface(dir):
            return {(2 + 2j) + dir * 2 + ((1 + 1j) - (abs(dir.real) + (abs(dir.imag) * 1j))) * x for x in [-2,-1, 0, 1,2]}

        mapping = {}
        for i in range(5):
            for j in range(5):
                mapset = set()
                loc = i+(1j*j)

                for dir in DIRS:
                    mapset.add((loc+dir,0))

                    if loc == get_inner_interface(dir):
                        for outer_loc in get_outer_interface(dir):
                            mapset.add((outer_loc,-1))
                    if loc in get_outer_interface(dir):
                        mapset.add((get_inner_interface(dir),1))

                mapset -= {(2+2j,0)} # center piece does not exist
                mapping[loc] = mapset
        return mapping


    mapping = get_mapping()
    bugs = set()
    inp = read_input_lines()
    for i in range(5):
        for j in range(5):
            if inp[i][j] == '#':
                bugs.add((i+(1j*j),0))

    for iter in range(200):
        nextbugs = set()
        for level in range(min((x[1] for x in bugs))-1,max((x[1] for x in bugs))+2):
            for i in range(5):
                for j in range(5):
                    if not ((i==2) and (j==2)):
                        loc = i + (1j * j)
                        count = 0
                        for ajacent_loc, delta_level in mapping[loc]:
                            if (ajacent_loc,level+delta_level) in bugs:
                                count+=1
                        if (loc,level) in bugs and count == 1:
                            nextbugs.add((loc,level))
                        elif ((loc,level) not in bugs) and count in (1, 2):
                            nextbugs.add((loc,level))
        bugs = nextbugs
    print(len(bugs)) # 2221 too high

part_b()