data = open('day01_input.txt')
lines = data.readlines()
lines1 = [int(x.strip()) for x in lines]
def part_1(inp):
    f = sum([x//3-2 for x in inp if x > 8])
    return f
print(part_1(lines1))

fuel=0
def part_2(inp,fuel):
    f = [x // 3 - 2 for x in inp if x > 8]
    f1 = sum(f)
    fuel += sum(f)
    if len(inp)*8 < f1:
        return part_2(f,fuel)
    else:
        return f,fuel
print(part_2(lines1,fuel))
