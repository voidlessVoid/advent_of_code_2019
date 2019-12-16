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
    def get_pattern_index(i, r):
       return (i+1)//(r+1)

    number = read_input_text()
    pattern = [0, 1, 0, -1]
    for r in range(100):
        new_number = []
        for digit in range(len(number)):
            new_number.append(str(sum([(pattern[get_pattern_index(i,digit)%len(pattern)] * int(number[i])) for i in range(len(number))]))[-1])
        number = new_number
    print("".join(number)[:8])
#part_a()
def part_b_try_1():
    number = [int(x) for x in "03036732577212944063491565474664" * 10000 ]#read_input_text()*10000]
    for _ in range(100):
        new_number = []
        for digit in range(len(number)):
            s = 0
            sign = 1
            ix = digit # first digit with a 1
            while ix < (len(number)+1):
                s+= sum([x for x in number[ix:ix+digit+1]])*sign
                ix += 2+2*digit
                sign *=-1
            new_number.append(int(str(s)[-1]))
        print(_)
        number = new_number
    #print("".join(number)[:8])
    print("".join(number)[int("".join(number[:7])):][:8])

def part_b_try_2():
    number = [int(x) for x in "03036732577212944063491565474664"*10000 ]#read_input_text()*10000]

    def cashing_decorator(f):
        answers = {}
        def decorated(i,d):
            if (i, d) not in answers:
                answers[(i, d)] = f(i,d)
            return answers[(i,d)]
        return  decorated

    @cashing_decorator
    def solve_one(i,r):
        if r == 0:
            return number[i]
        else:
            s = 0
            sign = 1
            ix = i # first digit with a 1
            while ix < (len(number)+1):
                s+= sum([solve_one(i_above,r-1) for i_above in range(ix,min([ix+i+1,len(number)]))])*sign
                ix += 2+2*i
                sign *=-1
            return int(str(s)[-1])

    #print([solve_one(i,100) for i in range(8)])

    list_i = [int(x) for x in number[:7]]
    print(''.join([solve_one(i,100) for i in list_i]))


def part_b_try_3():
    str_num = read_input_text()
    base_i = int(str_num[:7])
    number = [int(x) for x in str_num *10000][base_i:]#read_input_text()*10000]

    for _ in range(100):
        sum_all = sum(number)
        new_number = []
        for i in range(len(number)):
            new_number.append(int(str(sum_all)[-1]))
            sum_all -= number[i]
        number = new_number

    print(number[:8])

part_b_try_3()