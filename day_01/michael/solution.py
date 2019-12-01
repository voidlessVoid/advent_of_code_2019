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
    print(sum([int(float(x)/3) -2 for x in read_input_lines()]))

def part_b():
    def get_fuel(x):
        fuel = 0
        while True:
            x = int(x/3)-2
            if x < 1:
                break
            fuel += x
        return fuel

    print(sum([get_fuel(float(x)) for x in read_input_lines()]))


part_b()