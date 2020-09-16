import os
import re
import sys
import pandas as pd
import numpy as np
import re
import os.path
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle,combinations

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = read_input_lines()

planet_dict = defaultdict()
def get_gravity(dictionary_of_planets, active_planet):

    list_of_planets = ['Io', 'Eu', 'Ga', 'Ca']
    list_of_inactive_planets = list_of_planets.copy()
    list_of_inactive_planets.remove(active_planet)

    x,y,z = dictionary_of_planets[active_planet][0][0],dictionary_of_planets[active_planet][1][0], dictionary_of_planets[active_planet][2][0]
    x1,x2,x3 = dictionary_of_planets[list_of_inactive_planets[0]][0][0], dictionary_of_planets[list_of_inactive_planets[1]][0][0], dictionary_of_planets[list_of_inactive_planets[2]][0][0]
    y1,y2,y3 = dictionary_of_planets[list_of_inactive_planets[0]][1][0], dictionary_of_planets[list_of_inactive_planets[1]][1][0], dictionary_of_planets[list_of_inactive_planets[2]][1][0]
    z1,z2,z3 = dictionary_of_planets[list_of_inactive_planets[0]][2][0], dictionary_of_planets[list_of_inactive_planets[1]][2][0], dictionary_of_planets[list_of_inactive_planets[2]][2][0]
    x_array = np.array([x1,x2,x3])
    y_array = np.array([y1,y2,y3])
    z_array = np.array([int(z1),int(z2),int(z3)])
    x_grav = -np.sum(np.greater_equal(x,x_array))+3-np.sum(np.greater_equal(x,x_array))+np.sum(np.equal(x,x_array))
    y_grav = -np.sum(np.greater_equal(y,y_array))+3-np.sum(np.greater_equal(y,y_array))+np.sum(np.equal(y,y_array))
    z_grav = -np.sum(np.greater_equal(z,z_array))+3-np.sum(np.greater_equal(z,z_array))+np.sum(np.equal(z,z_array))

    return x_grav,y_grav,z_grav

def get_gravity_2(dictionary_of_planets, active_planet,axis): #axis can be x = 0,y = 1 or z = 2
    list_of_planets = ['Io', 'Eu', 'Ga', 'Ca']
    list_of_inactive_planets = list_of_planets.copy()
    list_of_inactive_planets.remove(active_planet)

    x = dictionary_of_planets[active_planet][axis][0]
    x1, x2, x3 = dictionary_of_planets[list_of_inactive_planets[0]][axis][0], \
                 dictionary_of_planets[list_of_inactive_planets[1]][axis][0], \
                 dictionary_of_planets[list_of_inactive_planets[2]][axis][0]
    x_array = np.array([x1, x2, x3])
    x_grav = -np.sum(np.greater_equal(x, x_array)) + 3 - np.sum(np.greater_equal(x, x_array)) + np.sum(
        np.equal(x, x_array))
    return x_grav


def part_a(lines_input, number_of_steps):
    list_of_planets = ['Io', 'Eu', 'Ga', 'Ca']


    for i in lines_input:
        pos = re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+", i)
        x = [int(pos[0]), 0]
        y = [int(pos[1]), 0]
        z = [int(pos[2]), 0]
        pos_comp = [x, y, z]
        planet_dict[list_of_planets.pop(0)] = pos_comp
    counter = 0
    list_of_planets = ['Io', 'Eu', 'Ga', 'Ca']
    while counter < number_of_steps:

        for planet in list_of_planets: # for every planet get gravity and update the planet_dict with these new velocities
            x_change, y_change, z_change = get_gravity(planet_dict, planet)
            planet_dict[planet][0][1] += x_change
            planet_dict[planet][1][1] += y_change
            planet_dict[planet][2][1] += z_change
        for planet in list_of_planets: # update positions
            x_change_pos = planet_dict[planet][0][1] + planet_dict[planet][0][0]
            y_change_pos = planet_dict[planet][1][1] + planet_dict[planet][1][0]
            z_change_pos = planet_dict[planet][2][1] + planet_dict[planet][2][0]
            planet_dict[planet][0][0] = x_change_pos
            planet_dict[planet][1][0] = y_change_pos
            planet_dict[planet][2][0] = z_change_pos
        counter+=1
        if counter == number_of_steps:
            dict_of_energy = defaultdict()
            for planet in list_of_planets:
                pot = abs(planet_dict[planet][0][0]) + abs(planet_dict[planet][1][0]) + abs(planet_dict[planet][2][0])
                kin = abs(planet_dict[planet][0][1]) + abs(planet_dict[planet][1][1]) + abs(planet_dict[planet][2][1])
                tot = pot*kin
                dict_of_energy[planet] = tot
            print('energy: ', sum(dict_of_energy.values()) )


def part_b(lines_input,planet_dict_):
    list_of_planets = ['Io', 'Eu', 'Ga', 'Ca']
    periods=[]

    for i in lines_input:
        pos = re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+", i)  # use tuples instead of complex numbers
        x = [int(pos[0]), 0]
        y = [int(pos[1]), 0]
        z = [int(pos[2]), 0]
        pos_comp = [x, y, z]
        planet_dict_[list_of_planets.pop(0)] = pos_comp

    list_of_planets = ['Io', 'Eu', 'Ga', 'Ca']
    print(planet_dict_)
    initial_x = [planet_dict_[list_of_planets[0]][0][0], planet_dict_[list_of_planets[1]][0][0],planet_dict_[list_of_planets[2]][0][0],planet_dict_[list_of_planets[3]][0][0]]
    print('init_x',initial_x)
    initial_y = [planet_dict_[list_of_planets[0]][1][0], planet_dict_[list_of_planets[1]][1][0],planet_dict_[list_of_planets[2]][1][0],planet_dict_[list_of_planets[3]][1][0]]
    print('init_y', initial_y)
    initial_z = [planet_dict_[list_of_planets[0]][2][0], planet_dict_[list_of_planets[1]][2][0],planet_dict_[list_of_planets[2]][2][0],planet_dict_[list_of_planets[3]][2][0]]
    print('init_z', initial_z)
    for i in range(3):
        counter = 1
        timeloop = 0
        if i == 0:
            init = initial_x
        elif i == 1:
            init = initial_y
        else:
            init = initial_z

        while timeloop != 1:

            for planet in list_of_planets:  # for every planet get gravity and update the planet_dict with these new velocities
                x_change = get_gravity_2(planet_dict_, planet,i)
                planet_dict_[planet][i][1] += x_change
            for planet in list_of_planets:  # update positions
                x_change_pos = planet_dict_[planet][i][1] + planet_dict_[planet][i][0]
                planet_dict_[planet][i][0] = x_change_pos
            counter += 1
            now_state = [planet_dict_[list_of_planets[0]][i][0], planet_dict_[list_of_planets[1]][i][0],planet_dict_[list_of_planets[2]][i][0],planet_dict_[list_of_planets[3]][i][0]]
            if now_state == init:
                periods.append(counter)
                timeloop = 1
                print('timeloop at step: ', counter)
    print(periods)
    print(np.lcm.reduce(periods))

part_a(lines, 1000)
# correct answer: 12053
part_b(lines,planet_dict)
# correct answer: [186028, 286332, 96236] 320380285873116
