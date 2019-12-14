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


def part_a(req={'FUEL':1}):
    reactions =[["".join([y for y in x if y.isalnum()]) for x in z.split()] for z in read_input_lines()]
    reactions = [[x for x in y if x] for y in reactions] #remove empty strings
    reactiondict = {}
    for reaction in reactions:
        x = list(zip(reaction[1::2],[int(x) for x in reaction[::2]]))
        reactiondict[x[-1][0]] = (x[-1][1],x[:-1]) #every product linked to a tuple of # of product and ingredients

    wishlist = req
    extra_coomponents=defaultdict(int)
    while set(wishlist) - {'ORE'}:
        for item in list(wishlist.keys()):
            if item != 'ORE':
                if wishlist[item] < extra_coomponents[item]:
                    extra_coomponents[item] -= wishlist[item]
                else:
                    required = wishlist[item] - extra_coomponents[item]
                    extra_coomponents[item] = 0
                    reaction = reactiondict[item]
                    runs = math.ceil(required/reaction[0])
                    produced = runs * reaction[0]
                    extra_coomponents[item] += produced-required

                    for ingredient, quantity in reaction[1]:
                        if ingredient in wishlist:
                            wishlist[ingredient]+= quantity * runs
                        else:
                            wishlist[ingredient] = quantity * runs
                del wishlist[item]
    return(wishlist['ORE'])

print(part_a())




def part_b():
    ore = 1000000000000
    estimate_window = [ore//248794,ore]
    while estimate_window[0] != estimate_window[1]:
        middle = math.ceil(sum(estimate_window)/2)
        ore_req = part_a({"FUEL":middle})
        if ore_req > ore:
            estimate_window[1] = middle-1
        else:
            estimate_window[0] = middle
    print(estimate_window[0])

part_b()
