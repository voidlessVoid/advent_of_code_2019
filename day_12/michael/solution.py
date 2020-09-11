import os
import numpy as np
import operator
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
    moon_to_coords = lambda x: np.array([float(y.split('=')[1]) for y in x.strip("<>").split(",")])
    moons = read_input_lines()
    moon_coords = np.array([moon_to_coords(x) for x in moons])
    moon_velocities = np.zeros(moon_coords.shape)

    for step in range(1000):
        print(moon_coords)
        print(' ')
        for moonindex in range(len(moons)):
            moon_velocities[moonindex,:] += np.sum(moon_coords > moon_coords[[moonindex],:], axis = 0)
            moon_velocities[moonindex,:] -= np.sum(moon_coords < moon_coords[[moonindex],:], axis = 0)
        moon_coords += moon_velocities

    moon_velocities = np.abs(moon_velocities)
    moon_coords = np.abs(moon_coords)
    print(np.sum(np.sum(moon_velocities,axis=1) * np.sum(moon_coords, axis=1)))

#part_a()


def part_b_naive(): # does not finish in reasonable time!
    def hash_states (moon_coords,moon_velocities):
        return hash(str(moon_coords) + str(moon_velocities))

    moon_to_coords = lambda x: np.array([float(y.split('=')[1]) for y in x.strip("<>").split(",")])
    moons = read_input_lines()
    moon_coords = np.array([moon_to_coords(x) for x in moons])
    moon_velocities = np.zeros(moon_coords.shape)
    states = {hash_states(moon_coords,moon_velocities)}

    for step in range(10**100):
        for moonindex in range(len(moons)):
            moon_velocities[moonindex, :] += np.sum(moon_coords > moon_coords[[moonindex], :], axis=0)
            moon_velocities[moonindex, :] -= np.sum(moon_coords < moon_coords[[moonindex], :], axis=0)
        moon_coords += moon_velocities

        hashing = hash_states (moon_coords,moon_velocities)
        if hashing in states:
            break

    print(step)

def part_b():
    def stringify_state(moon_coords, moon_velocities):
        return "_".join([str(int(x)) for x in (list(moon_coords) + list(moon_velocities))])

    moon_to_coords = lambda x: np.array([float(y.split('=')[1]) for y in x.strip("<>").split(",")])
    moons = read_input_lines()
    moon_coords = np.array([moon_to_coords(x) for x in moons])
    moon_velocities = np.zeros(moon_coords.shape)

    periods = []
    for dim in range(3): # for every dim see what the period is

        dim_coords = moon_coords[:,dim].flatten()
        dim_velocities = moon_velocities[:,dim].flatten()
        states = {stringify_state(dim_coords,dim_velocities):0}
        for i in range(1,10**10):
            dim_velocities += np.array([sum(dim_coords > x) for x in dim_coords]).flatten()
            dim_velocities -= np.array([sum(dim_coords < x) for x in dim_coords]).flatten()
            dim_coords += dim_velocities
            str_state = stringify_state(dim_coords,dim_velocities)
            if str_state in states:
                print(f'found period at iter {i} of period {i - states[str_state]}') #finding: i == period
                break
            states[str_state] = i
        periods.append(i)

    #now we find the smallest period of time that is devisible by all the axis-specific periods
    prod_periods = int(reduce(operator.mul,periods)) #this is an upper bound
    best = prod_periods
    for x in range(max(periods),prod_periods+1,max(periods)): # here we find the smallest. Brute force but works (eventually)
        for period in periods:
            if x%period != 0:
                break
        else:
            best = x
            break
    print(best) # 303459551979256

part_b()