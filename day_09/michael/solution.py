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

class opcode_machine():
    int2len = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 2}

    def  __init__(self,codelist,inp):
        self.codelist = defaultdict(int)
        for i, v in enumerate(codelist):
            self.codelist[i] = v

        self.inp = deque(inp)
        self.i=0
        self.outputlist = deque()
        self.relative_base = 0
        self.mode2value = {
           1 : lambda x: x,
           0 : lambda x: self.codelist[x],
           2: lambda x: self.codelist[self.relative_base + x]}

        self.mode2value_literal = {
           1 : lambda x: x,
           0 : lambda x: x,
           2: lambda x: self.relative_base + x}

        self.get = lambda val, mode: self.mode2value[mode](val)
        self.get_literal = lambda val, mode: self.mode2value_literal[mode](val)

        self.int2func = {
                        1: self.add,
                        2: self.mul,
                        3: self.input,
                        4: self.output,
                        5: self.JIT,
                        6: self.JIF,
                        7: self.LT,
                        8: self.EQ,
                        9: self.ARB}

    def put(self,place,val):
        self.codelist[place] = val

    def add(self,values, modes):
        a = self.get(values[0], modes.pop())
        b = self.get(values[1], modes.pop())
        c = self.get_literal(values[2], modes.pop())
        self.put(c,a+b)

    def mul(self,values, modes):
        a = self.get(values[0], modes.pop())
        b = self.get(values[1], modes.pop())
        c = self.get_literal(values[2], modes.pop())
        self.put(c,a*b)

    def input(self,values, modes):
        place = self.get_literal(values[0],modes.pop())
        self.put(place, self.inp.pop())

    def output(self,values, modes):
        self.outputlist.append(self.get(values[0], modes.pop()))
        return 'wait'

    def JIT(self,values, modes):
        if self.get(values[0],modes.pop())!= 0:
            self.i = self.get(values[1],modes.pop())
            return 'jumped'

    def JIF(self,values, modes):
        if self.get(values[0],modes.pop())== 0:
            self.i = self.get(values[1],modes.pop())
            return 'jumped'

    def LT(self, values, modes):
        a = self.get(values[0], modes.pop())
        b = self.get(values[1], modes.pop())
        c = self.get_literal(values[2], modes.pop())
        if a < b:
            self.put(c,1)
        else:
            self.put(c,0)

    def EQ(self, values, modes):
        a = self.get(values[0], modes.pop())
        b = self.get(values[1], modes.pop())
        c = self.get_literal(values[2], modes.pop())
        if  a == b:
            #put(get(values[2], modes.pop(0)), 1)
            self.put(c,1)
        else:
            #put(get(values[2], modes.pop(0)), 0)
            self.put(c,0)

    def ARB(self,values,modes): # ajust relative base
        self.relative_base += self.get(values[0],modes.pop())

    def run(self):
        while self.codelist[self.i] != 99:
            opcode = self.codelist[self.i]
            op = int(str(opcode)[-2:])
            modes = [int(x) for x in
                     str(opcode)[:-2].zfill(4)]  # add extra 0 at the front for in case modes are missing
            func = self.int2func[op]
            values = [self.codelist[x] for x in range(self.i+1,self.i+self.int2len[op])]
            special_return_value = func(values, modes)
            if not special_return_value == 'jumped':
                self.i+= self.int2len[op]
            #if special_return_value == 'wait':
            #    return


        return(True)

def part_a():
    c = read_input_text()
    code = [int(x) for x in c.split(',')]
    opcode_machine_instance = opcode_machine(code,[1])
    opcode_machine_instance.run()
    print(opcode_machine_instance.outputlist)

def part_b():
    c = read_input_text()
    code = [int(x) for x in c.split(',')]
    opcode_machine_instance = opcode_machine(code, [2])
    opcode_machine_instance.run()
    print(opcode_machine_instance.outputlist)

part_b()