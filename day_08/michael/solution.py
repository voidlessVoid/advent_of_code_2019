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
    pixels = read_input_text()
    width, height = 25, 6
    layers = [pixels[i:i+width*height] for i in range(0,len(pixels),width*height)]
    counters = [Counter(layer) for layer in layers]
    relevant_counter = sorted(counters,key =lambda x: x['0'])[0]
    print(relevant_counter['1']*relevant_counter['2'])
part_a()

def part_b():
    pixels = read_input_text()
    width, height = 25, 6
    layers = [pixels[i:i + width * height] for i in range(0, len(pixels), width * height)]

    final_layer = ['2']*(width*height)
    for layer in layers[::-1]:
        for i in range(width*height):
            if layer[i] != '2':
                final_layer[i] = layer[i]

    rows = [final_layer[i:i+width] for i in range(0,width*height,width)]
    for row in rows:
        print(' '.join([' ' if x == '0' else 'x' for x in row]))

part_b()
