import os
from itertools import permutations

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
        8: 4}

    def  __init__(self,codelist,inp):
        self.codelist = codelist
        self.inp = inp
        self.i=0
        self.outputlist = []
        self.mode2value = {
           1 : lambda x: x,
           0 : lambda x: self.codelist[x]}

        self.get = lambda val, mode: self.mode2value[mode](val)
        self.int2func = {
                        1: self.add,
                        2: self.mul,
                        3: self.input,
                        4: self.output,
                        5: self.JIT,
                        6: self.JIF,
                        7: self.LT,
                        8: self.EQ}

    def put(self,place,val):
        self.codelist[place] = val

    def add(self,values, modes):
        a = self.get(values[0], modes.pop())
        b = self.get(values[1], modes.pop())
        self.put(values[2],a+b)

    def mul(self,values, modes):
        a = self.get(values[0], modes.pop())
        b = self.get(values[1], modes.pop())
        self.put(values[2],a*b)

    def input(self,values, modes):
        self.put(values[0], self.inp.pop())

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
        if a < b:
            self.put(values[2],1)
        else:
            self.put(values[2],0)

    def EQ(self, values, modes):
        a = self.get(values[0], modes.pop())
        b = self.get(values[1], modes.pop())
        if  a == b:
            #put(get(values[2], modes.pop(0)), 1)
            self.put(values[2],1)
        else:
            #put(get(values[2], modes.pop(0)), 0)
            self.put(values[2],0)

    def run(self):
        while self.codelist[self.i] != 99:
            opcode = self.codelist[self.i]
            op = int(str(opcode)[-2:])
            modes = [int(x) for x in
                     str(opcode)[:-2].zfill(4)]  # add extra 0 at the front for in case modes are missing
            func = self.int2func[op]
            values = self.codelist[self.i + 1:self.i+ self.int2len[op]]
            special_return_value = func(values, modes)
            if not special_return_value == 'jumped':
                self.i+= self.int2len[op]
            if special_return_value == 'wait':
                return


        return(True)

    def __repr__(self):
        return f'intcode machine number {self.instancenumber} is extremely happy to be alive!'

def part_a():
    def opt_signal(input_signal,possible_phase_settings):
        best = -float('inf')
        if not possible_phase_settings:
            return input_signal
        for setting in possible_phase_settings:
            codes = [int(x) for x in read_input_text().split(',')]
            machine = opcode_machine(codes, [input_signal, setting])
            machine.run()
            next_stage_signal = machine.outputlist[-1]
            final_signal = opt_signal(next_stage_signal,possible_phase_settings-{setting})
            if final_signal > best:
                best = final_signal
        return best

    print(opt_signal(0,set(range(5))))

part_a()
def part_b():
    codes = [int(x) for x in read_input_text().split(',')]
    best = -float('inf')
    for setting_map in (permutations(range(5,10))):
        machines = [opcode_machine(codes[::], []) for x in range(5)]
        output_signals = [0] * 5
        active_machine = 0
        for setting, machine in zip(setting_map,machines):
            machine.inp = [setting]
        machines[active_machine].inp = [0] + machines[active_machine].inp

        while True:
            hit_99 = machines[active_machine].run()
            if hit_99: # we hit a 99
                break
            else:
                next_active_machine = (active_machine + 1) % 5
                machines[next_active_machine].inp =machines[active_machine].outputlist + machines[next_active_machine].inp
                output_signals[active_machine] = machines[active_machine].outputlist[-1]
                machines[active_machine].outputlist = []
                active_machine = next_active_machine

        if output_signals[4] > best:
            best = output_signals[4]

    print(best)

part_b()