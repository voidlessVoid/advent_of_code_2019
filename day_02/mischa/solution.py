data = open('day02_input.txt')
lines = data.readline().split(',')
lines1 = [int(x) for x in lines if x.isnumeric()]

def part_1(inp, noun, verb):
    copy = inp.copy()
    i = 0
    copy[1] = int(noun)
    copy[2] = int(verb)
    while i <= len(copy)-4:
        loc1, loc2, new_loc = copy[i + 1], copy[i + 2], copy[i + 3]
        if copy[i] == 99:
            break
        elif copy[i] == 1:
            new = copy[loc1] + copy[loc2]
            copy[new_loc] = new
            i +=4
        elif inp[i] == 2:
            new = copy[loc1] * copy[loc2]
            copy[new_loc] = new
            i += 4
    return copy[0]
print(part_1(lines1,12,2))

def part_2(inp):
    score = 19690720
    n,v,sc=0,0,0
    while sc < score:
        n += 1
        sc = part_1(inp,n,v)
    n -=1
    sc=0
    while sc < score:
        v += 1
        sc = part_1(inp, n, v)
    return (n,v),(n*100+v)
print(part_2(lines1))
