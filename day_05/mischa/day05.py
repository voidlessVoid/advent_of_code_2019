data = open('day05_input.txt')
lines = data.readline().split(',')
lines1  = [int(x.strip()) for x in lines]


def get_opcode_mode(i):
    instr = str(i).zfill(5)
    op_code = instr[-2:]
    par1,par2,par3 = instr[-3],instr[-4],instr[-5]
    return op_code, par1,par2,par3


def get_par(copy_l, op, mode,count,par_num):

    if int(mode) == 0 and int(op) !=3 and int(op)!=4 and int(par_num) !=3:
        x = copy_l[count+par_num]
        return copy_l[x]
    else:
        return copy_l[count+par_num]

def part_1(inp, inp_num):
    copy = inp.copy()
    i = 0
    last_output= ''
    while i <= len(copy)-2 and copy[i] !=99:
        op, mod1,mod2,mod3 = get_opcode_mode(copy[i])
        par1 = get_par(copy,op,mod1,i,1)
        par2 = get_par(copy,op,mod2,i,2)
        par3 = copy[i+3]
        if int(op) == 1:
            new = par1 + par2
            copy[par3] = new
            i +=4
        elif int(op) == 2:
            new = par1 * par2
            copy[par3] = new
            i += 4
        elif int(op) == 3:
            copy[par1] = inp_num
            i += 2
        elif int(op) == 4:
            last_output = copy[par1]
            i += 2
        elif int(op) ==5:
            if int(par1) != 0:
                i = int(par2)
            else:
                i +=3
        elif int(op) ==6:
            if int(par1) == 0:
                i = int(par2)
            else:
                i +=3
        elif int(op) ==7:
            if int(par1) < int(par2):
                copy[par3] = 1
            else:
                copy[par3] = 0
            i += 4
        elif int(op) ==8:
            if int(par1) == int(par2):
                copy[par3] = 1
            else:
                print(par3)
                copy[par3] = 0
            i += 4
    return last_output

#part1
print(part_1(lines1,1))
#part2
print(part_1(lines1,5))



