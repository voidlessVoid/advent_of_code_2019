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


def part_a(inp = 1):
    outputlist = []
    get = lambda val, mode: mode2value[mode](val)
    def put(place,val):
        codelist[place] = val

    mode2value = {
        1 : lambda x: x,
        0 : lambda x: codelist[x]
    }

    def add(values, modes):
        a = get(values[0], modes.pop(0))
        b = get(values[1], modes.pop(0))
        put(values[2],a+b)

    def mul(values, modes):
        a = get(values[0], modes.pop(0))
        b = get(values[1], modes.pop(0))
        put(values[2],a*b)

    def input(values, modes):
        put(values[0], inp)

    def output(values, modes):
        outputlist.append(get(values[0], modes.pop(0)))

    def JIT(values, modes):
        if get(values[0],modes.pop(0))!= 0:
            i[0] = get(values[1],modes.pop(0))
            return True

    def JIF(values, modes):
        if get(values[0],modes.pop(0))== 0:
            i[0] = get(values[1],modes.pop(0))
            return True

    def LT(values, modes):
        a = get(values[0], modes.pop(0))
        b = get(values[1], modes.pop(0))
        if a < b:
            #put(get(values[2], modes.pop(0)), 1)
            put(values[2],1)
        else:
            #put(get(values[2], modes.pop(0)), 0)
            put(values[2],0)

    def EQ(values, modes):
        a = get(values[0], modes.pop(0))
        b = get(values[1], modes.pop(0))
        if  a == b:
            #put(get(values[2], modes.pop(0)), 1)
            put(values[2],1)
        else:
            #put(get(values[2], modes.pop(0)), 0)
            put(values[2],0)

    int2func = {
        1: add,
        2: mul,
        3: input,
        4: output,
        5: JIT,
        6: JIF,
        7: LT,
        8: EQ}

    int2len = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4
    }

    #codelist = [int(x.strip()) for x in """3,9,7,9,10,9,4,9,99,-1,8""".split(',')]
    codelist = [int(x.strip()) for x in read_input_text().split(',')]


    i = [0]
    while codelist[i[0]] != 99:
        opcode = codelist[i[0]]
        op = int(str(opcode)[-2:])
        modes = [int(x) for x in str(opcode)[:-2][::-1]] + ([0] * 4) #add extra 0 at the end for if fewer modes are given
        func = int2func[op]
        values = codelist[i[0]+1:i[0]+int2len[op]]
        jumped = func(values,modes)
        if not jumped:
            i[0]+= int2len[op]
        print(i, codelist)


    print(outputlist)


def part_b():
    part_a(inp=5)

part_b()