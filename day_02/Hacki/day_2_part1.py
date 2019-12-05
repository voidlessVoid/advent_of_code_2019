"""An Intcode program is a list.txt of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0).

Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt.
Encountering an unknown opcode means something went wrong.


1 : Opcode 1 adds together numbers read from two positions and stores the result in a third position.

    -  The three integers immediately after the opcode tell you these three positions
    -  the first two indicate the positions from which you should read the input values,
    -  and the third indicates the position at which the output should be stored.


    For example, if your Intcode computer encounters 1,10,20,30,
    it should read the values at positions 10 and 20, add those values,
    and then overwrite the value at position 30 with their sum.


2 : Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
    - Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions."""




ls = open('list.txt', 'r')

for line in ls.readlines():
    ls = line.rstrip().split(',')
    ls = [int(i) for i in ls]

ls[1] = 12
ls[2] = 2

position = 0
snap = 4

while ls[position] != 99:
    opcode = {1 : ls[ls[position + 1]] + ls[ls[position + 2]],
              2 : ls[ls[position + 1]] * ls[ls[position + 2]]}
    calc = opcode[ls[position]]
    ls[ls[position + snap - 1]] = calc
    position += snap
print(ls)


