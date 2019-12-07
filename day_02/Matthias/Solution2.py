import sys

def opcode_1(next_index, secondnext_index, thirdnext_index):
    print "Running opcode_1"
    pos1 = lst[next_index]
    pos2 = lst[secondnext_index]
    summe = lst[pos1] + lst[pos2]
    lst[thirdnext_index] = summe
    print "Calculated sum of %f" % (summe)
    
def opcode_2(next_index, secondnext_index, thirdnext_index):
    print "Running opcode_2"
    pos1 = lst[next_index]
    pos2 = lst[secondnext_index]
    product = lst[pos1] * lst[pos2]
    lst[thirdnext_index] = product

lst = []

# Read the input file as a list
with open("Input.txt") as f:    
    inputstuff = f.readlines()
    items = inputstuff[0].split(",")
    for item in items:
        lst.append(int(item))

# For loop for different opcodes
for number in lst:
    current_index = lst.index(number)
    condition = current_index % 4
    next_index = current_index + 1
    secondnext_index = current_index + 2
    thirdnext_index = current_index + 3
    fourthnext_index = current_index + 4    

    if condition != 0:
        pass
    else:
        if number == 1:
            opcode_1(next_index, secondnext_index, thirdnext_index)
        elif number == 2:
            opcode_2(next_index, secondnext_index, thirdnext_index)
        elif number == 99:
            print lst
            sys.exit()
        else:
            pass
    print number

print lst
