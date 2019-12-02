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
    int2fuc = {1: operator.add, 2: operator.mul}
    opcodes = [int(x.strip()) for x in read_input_text().split(",")]
    i = 0
    opcodes[1, 2] = 12 , 2
    while opcodes[i] != 99:
        a,b,c,d = opcodes[i:i+4]
        opcodes[d] = int2fuc[a](opcodes[c],opcodes[b])
        i+=4

    print(opcodes[0])

def part_b():
    def get_function():
        opcodes = [int(x.strip()) for x in read_input_text().split(",")]
        int2fuc = {1: operator.add, 2: operator.mul}
        num2symbol = {1:'+', 2:'*'}
        funclist = deepcopy(opcodes)
        funclist[1] = "a"
        funclist[2] = "b"
        i=0
        opcodes[1] = 12
        opcodes[2] = 2
        while opcodes[i] != 99:
            a, b, c, d = opcodes[i:i + 4]
            opcodes[d] = int2fuc[a](opcodes[c], opcodes[b])
            funclist[d] = f"({funclist[b]} {num2symbol[a]} {funclist[c]})"
            i += 4
        print(funclist[0])
        #(3 + ((1 + (3 * (1 + ((3 + (3 + (5 * (2 * (4 + ((5 * (1 + ((5 * (1 + (2 * ((4 * ((((2 + (5 + (2 + (a * 4)))) + 4) + 2) + 5)) + 2)))) * 3))) + 1)))))) * 3)))) + b))
        # wolfram alpha -> b = 18576009 - 216000 a
        # a = 86, b= 9
    get_function()

part_b()