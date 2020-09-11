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
            self.put(c,1)
        else:
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
            if special_return_value == 'wait':
                return

        return(True)

    def return_copy(self):
        copy = opcode_machine([],[])
        copy.codelist = deepcopy(self.codelist)
        copy.i = self.i
        copy.relative_base = self.relative_base
        return copy


def part_a():
    code = [int(x) for x in read_input_text().split(",")]
    machine = opcode_machine(code,[])
    i = 0
    object_dict = {}

    dir_dict={ord('<'): -1j,
              ord('>'): 1j,
              ord('^'):-1,
              ord('v') : 1}

    while True:
        halt = machine.run()
        if halt:
            break
        output = machine.outputlist.pop()
        if output == 35:
            object_dict[i] = "#"
        if output in dir_dict:
            direction = output
            location = i
        if output == 10:
            i = i.real + 1
        else:
            i+= 1j

    intersections = {i for i in object_dict if all(i+d in object_dict for d in {1,-1,1j,-1j})}
    print('part a: ',sum(i.real*i.imag for i in intersections))
    return object_dict, location, direction

#part_a()

def visualize():
    with open('map.txt','w') as fh:
        map, loc, dir = part_a()
        print(loc)
        for row in range(int(min([i.real for i in map])),int(max([i.real for i in map]))+1):
            out = []
            for col in range(int(min([i.imag for i in map])),int(max([i.imag for i in map]))+1):
                if row+col*1j in map:
                    out.append('#')
                else:
                    out.append('.')
            out.append('\n')
            fh.write("".join(out))


#visualize()

def part_b():
    """ the map does not contain tripple points and has two endpoints, on one of which you start.
    We construct a path such that the robot always continues in the same direction until it cant,
     then pics the one direction that works """
    dir_dict={ord('<'): -1j,
              ord('>'): 1j,
              ord('^'):-1,
              ord('v') : 1}


    next_dir = {
        ord('<'): {"L": ord('v'), "R": ord('^')},
        ord('>'):{"L": ord('^'), "R": ord('v')},
        ord('^'): {"L": ord('<'), "R": ord('>')},
        ord('v'): {"L": ord('>'), "R": ord('<')}
    }

    map, loc, dir = part_a()
    visited = {loc}
    instructions = []
    while set(map)-visited:
        if loc + dir_dict[dir] not in map:
            for command, next in next_dir[dir].items():
                if loc+dir_dict[next] in map:
                    instructions.append(command)
                    dir = next
        loc += dir_dict[dir]
        visited.add(loc)
        instructions.append(1)
    instructions = "".join([str(x) for x in instructions])
    print(instructions)

    def collapse_instruction(instr):
        out = []
        count = 0
        for x in instr:
            if x in "RL":
                if count > 0:
                    out.append(ord(','))
                    out.extend([ord(x) for x in str(count)])
                    count = 0
                out.append(ord(','))
                out.append(ord(x))

            else:
                count += 1
        if count > 0:
            out.append(ord(','))
            out.extend([ord(x) for x in str(count)])
        return out[1:] #skip firt comma

    #chunks = [chunk for chunk in chunks if len(collapse_instruction(chunk)) <=20]
    #chunks = {instructions[i:j] for i in range(len(instructions)) for j in range(i+1,len(instructions))} # brute force FTW
    chunks = {'R1111111111L11111111R1111111111R1111','L111111L111111R1111111111','L111111R111111111111R111111111111R1111111111'}
    def apply_chunks(instring,chunks, used, instructionlist):
        if len(instructionlist) > 10:
            return False
        if instring == '':
            return instructionlist
        for chunk in chunks:
            if instring.startswith(chunk):
                if ((len(used)) < 3) or (chunk in used):
                    ans = apply_chunks(instring[len(chunk):],chunks,used|{chunk}, instructionlist + [chunk])
                    if ans:
                        return ans

    instruction_list = apply_chunks(instructions,chunks, set(),[])
    print(instruction_list or 'not found')

    collapsed = [collapse_instruction(x) for x in instruction_list]
    print(collapsed)

    map = {'R1111111111L11111111R1111111111R1111':'A',
           'L111111L111111R1111111111':'B',
           'L111111R111111111111R111111111111R1111111111':'C'}

    main = []
    for num in [ord(map[x]) for x in instruction_list]:
        main.append(num)
        main.append(ord(','))
    main[-1] = 10
    A = collapsed[0] + [10]
    print(A)
    B = collapsed[1] + [10]
    C = collapsed[3] + [10]

    code = [int(x) for x in read_input_text().split(",")]
    code[0] = 2
    machine = opcode_machine(code,(main+A+B+C+[ord('n'),10])[::-1])

    halt = False
    while not halt:
        halt = machine.run()

    print(''.join([chr(x) for x in  list(machine.outputlist)]))
    print(machine.outputlist.pop())

part_b()






