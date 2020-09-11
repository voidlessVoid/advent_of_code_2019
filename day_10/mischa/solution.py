
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

inp = read_input_lines()
dict_of_ast = defaultdict()
list_of_detectable_ast = []
def part_a(input_list):
    count = 0
    target_ast = 0
    max_len = 0
    dict_of_angles_of_target_ast = {}
    for i in range(len(input_list)):# y make a dictionary with all asteroids
        for x in range(len(input_list[i])): # x
            if input_list[i][x]=='#':
                asteroid = (x,i)
                dict_of_ast[count] = asteroid
                count+=1

    for y in dict_of_ast:# go through all asteroids
        active_asteroid = y
        dict_of_angles = {}
        for a in dict_of_ast: # make a dictionary with all the asteroids with line of sight
            new_x = dict_of_ast[a][1]-dict_of_ast[active_asteroid][1]
            new_y= dict_of_ast[a][0]-dict_of_ast[active_asteroid][0]
            angle = round(math.atan2(new_y,new_x),5)
            dict_of_angles[angle] = a

        list_of_detectable_ast.append(len(dict_of_angles))
        if len(dict_of_angles) > max_len:
            dict_of_angles_of_target_ast = dict_of_angles
            max_len= len(dict_of_angles)
            target_ast = active_asteroid
    return max(list_of_detectable_ast), target_ast, dict_of_ast[target_ast], dict_of_angles_of_target_ast
answer_A, Laser_asteroid,coords_of_LaAst, dict_of_angles_of_LaserAsteroid = part_a(inp)

print('answer part A: ',answer_A)
#answer part A:221


def part_b(dict_of_angles_of_LaserAsteroid, dict_of_ast, LaserAsteroid_coords, LaserAsteroid):
    defaultdict_of_angles = defaultdict()
    for i in dict_of_ast:
        new_x = dict_of_ast[i][1] - dict_of_ast[LaserAsteroid][1]
        new_y = dict_of_ast[i][0] - dict_of_ast[LaserAsteroid][0]
        angle = round(math.atan2(new_y, new_x), 5)
        if angle in list(defaultdict_of_angles.keys()):
            defaultdict_of_angles[angle].append(i)
        else:
            defaultdict_of_angles[angle] = [i]

    dict_upper_left = defaultdict()
    dict_upper_right = defaultdict()
    dict_lower_left = defaultdict()
    dict_lower_right = defaultdict()

    for x in defaultdict_of_angles:
        if x >= 0:  # upper quadrant
            if x >= 1.5:  # upper upper_right
                dict_upper_right[x] = defaultdict_of_angles[x]
            else:  # upper lower_right
                dict_lower_right[x] = defaultdict_of_angles[x]
        else:
            if x < -1.5:  # upper_left quadrant
                dict_upper_left[x] = defaultdict_of_angles[x]
            else:  # lower left quadrant
                dict_lower_left[x] = defaultdict_of_angles[x]

    destroyd_asteroids_coords = []

    max_ast = 200
    while len(destroyd_asteroids_coords) <max_ast:
        sort_upper_left = sorted(dict_upper_left)
        sort_upper_right = sorted(dict_upper_right)
        sort_lower_left = sorted(dict_lower_left)
        sort_lower_right = sorted(dict_lower_right)
        len_upLe = len(dict_upper_left.keys())
        len_upRi = len(dict_upper_right)
        len_loLe = len(dict_lower_left)
        len_loRi = len(dict_lower_right)
        counter = 0
        for a in reversed(sort_upper_right):
            if len(dict_upper_right[a]) > 0 and counter < len_upRi and len(destroyd_asteroids_coords) <max_ast:
                destroyd_ast = dict_upper_right[a].pop(-1)
                destroyd_asteroids_coords.append(dict_of_ast[destroyd_ast])
            elif len(dict_upper_right[a]) <= 0 :
                del dict_upper_right[a]
            else:
                break
            counter +=1
        counter = 0
        for a in reversed(sort_lower_right) :
            if len(dict_lower_right[a]) > 0 and counter < len_loRi and len(destroyd_asteroids_coords) <max_ast:
                destroyd_ast = dict_lower_right[a].pop(-1)
                destroyd_asteroids_coords.append(dict_of_ast[destroyd_ast])
            elif len(dict_lower_right[a]) <= 0:
                del dict_lower_right[a]
            else:
                break
            counter += 1
        counter = 0
        for a in reversed(sort_lower_left) :
            if len(dict_lower_left[a]) > 0 and counter < len_loLe and len(destroyd_asteroids_coords) <max_ast:
                destroyd_ast = dict_lower_left[a].pop(-1)
                destroyd_asteroids_coords.append(dict_of_ast[destroyd_ast])
            elif len(dict_lower_left[a]) <= 0:
                del dict_lower_left[a]
            else:
                break
            counter += 1
        counter = 0
        for a in reversed(sort_upper_left):
            if len(dict_upper_left[a]) > 0 and counter < len_upLe and len(destroyd_asteroids_coords) <max_ast:
                destroyd_ast = dict_upper_left[a].pop(-1)
                destroyd_asteroids_coords.append(dict_of_ast[destroyd_ast])
            elif len(dict_upper_left[a]) <= 0:
                del dict_upper_left[a]
            else:
                break
            counter += 1

    twohundredAst = (destroyd_asteroids_coords[-1])
    answer = destroyd_asteroids_coords[-1][0]*100+destroyd_asteroids_coords[-1][1]
    return answer
answer_B = part_b(dict_of_angles_of_LaserAsteroid,dict_of_ast,coords_of_LaAst,Laser_asteroid)
print('answer part B: ',answer_B)