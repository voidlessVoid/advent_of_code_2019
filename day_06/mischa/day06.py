data  = open('day06_input.txt')
lines  = [x.strip() for x in data.readlines()]
lines1 = [x.split(')') for x in lines]

'''
functions
'''
def part_1(inp):
    inp1 = inp.copy()
    left = [x[0] for x in inp1]
    right = [x[1] for x in inp1]
    s_left, s_right = set(left), set(right)
    start = list(s_left.difference(s_right))
    end = list(s_right.difference(s_left))
    count, checksum, done = 0, 0, False
    distance, dis_count = 0, False
    while not done:
        if not end:
            done = True
        if dis_count:
            distance +=1
        planets_count = len(start)
        checksum += planets_count*count
        to_add=[]
        to_remove =[]
        for i in inp1:
            if i[0] in start and i[1] in end:
                to_add.append(i[1])
                to_remove.append(i)
            elif i[0] in start and i[1] not in end:
                to_remove.append(i)
        for i in to_remove:
            inp1.remove(i)

        left = [x[0] for x in inp1]
        right = [x[1] for x in inp1]
        s_left,s_right  = set(left),set(right)
        start = set(list(s_left.difference(s_right)))
        if to_add:
            for i in to_add:
                start.add(i)
        end = list(s_right.difference(s_left))
        count+=1
    return checksum
def get_orbiter(inp,star):
    closet_to = ''
    for i in inp:
        if star in i[1]:
            closet_to =i[0]
    return closet_to


def rec_walker(inp, me_pl, planets, counter):
    planets.append(me_pl)
    if me_pl == 'COM':
        return counter,planets
    else:
        counter+=1
        next_planet = get_orbiter(inp,me_pl)
        return rec_walker(inp, next_planet, planets, counter)

def part_2(inp1):
    me= 'YOU'
    santa= 'SAN'
    counter = 0
    planets_me_com = []
    planets_santa_com = []
    me_dist, me_pl = rec_walker(inp1, me, planets_me_com, counter)
    santa_dist, santa_pl = rec_walker(inp1, santa, planets_santa_com, counter)
    s_me_pl = set(me_pl)
    s_santa_pl = set(santa_pl)
    distance = s_me_pl.symmetric_difference(s_santa_pl)
    return len(distance)-2 #-2 because YOU and SANTA are ON the closest planet and do not have to travel TO this closest planet

'''
part 1
'''
print('part1: ',part_1(lines1))

'''
part 2
'''
print('part2: ',part_2(lines1))
#343