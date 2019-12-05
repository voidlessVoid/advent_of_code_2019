import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


class opcode_machine():
    instancecount = 0
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
        self.instancenumber = opcode_machine.instancecount
        opcode_machine.instancecount +=1
        self.codelist = codelist
        self.inp = inp
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
        self.put(values[0], self.inp)

    def output(self,values, modes):
        self.outputlist.append(self.get(values[0], modes.pop()))

    def JIT(self,values, modes):
        if self.get(values[0],modes.pop())!= 0:
            self.i = self.get(values[1],modes.pop())
            return True

    def JIF(self,values, modes):
        if self.get(values[0],modes.pop())== 0:
            self.i = self.get(values[1],modes.pop())
            return True

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
        self.i = 0
        while self.codelist[self.i] != 99:
            opcode = self.codelist[self.i]
            op = int(str(opcode)[-2:])
            modes = [int(x) for x in
                     str(opcode)[:-2].zfill(4)]  # add extra 0 at the front for in case modes are missing
            func = self.int2func[op]
            values = self.codelist[self.i + 1:self.i+ self.int2len[op]]
            jumped = func(values, modes)
            if not jumped:
                self.i+= self.int2len[op]

        print(self.outputlist[-1])

    def __repr__(self):
        return f'intcode machine number {self.instancenumber} is extremely happy to be alive!'
def part_a():
    codes = [int(x.strip()) for x in read_input_text().split(",")]
    machine = opcode_machine(codes,1)
    print(machine)
    machine.run()

def part_b():
    codes = [int(x.strip()) for x in read_input_text().split(",")]
    machine = opcode_machine(codes, 5)
    print(machine)
    machine.run()

part_a()
part_b()