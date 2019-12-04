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
    def valid(x):
        t = str(x)
        pair = any(t[i] == t[i+1] for i in range(len(t)-1))
        order = t == ''.join(sorted(t))
        return pair and order
    mi,ma = 278384,824795
    print(len([x for x in range(mi, ma+1) if valid(x)]))
#part_a()

def part_b():
    def valid(x):
        t = str(x)
        order = t == ''.join(sorted(t))

        countlist=[]
        lastchar = ''
        count = 0
        for char in t:
            if char == lastchar:
                count+=1
            else:
                countlist.append(count)
                lastchar = char
                count = 1
        countlist.append(count)

        return order and 2 in countlist

    mi, ma = 278384, 824795
    print(len([x for x in range(mi, ma + 1) if valid(x)]))
part_b()