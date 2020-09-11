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
from functools import lru_cache

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():

    def deal_into_new_stack(cards):
        cards.reverse()
        return cards

    def cut(cards, n):
        cards.rotate(-n)
        return cards

    def deal_with_increment(cards,n):
        new = [0] * 10007
        i=0
        while cards:
            new[i%10007] = cards.popleft()
            i+=n
        return deque(new)

    cards = deque(range(10007))
    instructions = read_input_lines()
    for instruction in instructions:
        if instruction.startswith('cut'):
            cards = cut(cards, int(instruction.split()[-1]))
        elif instruction.startswith('deal with increment'):
            cards = deal_with_increment(cards, int(instruction.split()[-1]))
        elif instruction.startswith('deal into new stack'):
            cards = deal_into_new_stack(cards)

    print(list(cards).index(2019))


def part_b_try_1():
    """ idea is we got back from index 2020 through each round of shuffeling"""
    n_cards =    119315717514047
    n_shuffles = 101741582076661

    def reverse_cut(index,n):
        return (index + n) % n_cards

    def reverse_stack(index):
        return n_cards - (index + 1)

    def reverse_increment(index,n):
        while True:
            if index % n == 0:
                return index // n
            index += n_cards

    def do_round(index):
        for instruction in instructions:
            if instruction.startswith('cut'):
                index = reverse_cut(index, int(instruction.split()[-1]))
            elif instruction.startswith('deal with increment'):
                index = reverse_increment(index, int(instruction.split()[-1]))
            elif instruction.startswith('deal into new stack'):
                index = reverse_stack(index)
        return index


    index = 2020
    instructions = read_input_lines()[::-1]
    indexes = set()
    for _ in range(100000):#n_shuffles):
        index = do_round(index)
        indexes.add(index)

    for index in indexes:
        for offset in range(1,1000):
            if index+ offset in indexes:
                print(index, offset)




    print(index)




def part_b_try_2():
    """ idea is we got back from index 2020 through each round of shuffeling"""
    n_cards =    119315717514047
    n_shuffles = 101741582076661

    class deck:
        def __init__(self):
            self.index = 0
            self.dir = 1
            self.stride = 1

        def reverse_cut(self,n):
            self.index = (self.index + n) % n_cards

        def reverse_stack(self):
            self.dir *= -1

        def reverse_increment(index,n):
            while True:
                if index % n == 0:
                    return index // n
                index += n_cards

    def do_round(index):
        for instruction in instructions:
            if instruction.startswith('cut'):
                index = index, int(instruction.split()[-1])
            elif instruction.startswith('deal with increment'):
                index = reverse_increment(index, int(instruction.split()[-1]))
            elif instruction.startswith('deal into new stack'):
                index = reverse_stack(index)
        return index


    index = 2020
    instructions = read_input_lines()[::-1]
    indexes = set()
    for _ in range(100000):#n_shuffles):
        index = do_round(index)
        indexes.add(index)

    for index in indexes:
        for offset in range(1,1000):
            if index+ offset in indexes:
                print(index, offset)


part_b()