import os
import heapq
from collections import Counter, ChainMap, defaultdict, deque


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines(path = 'input.txt'):
    with open(path, 'r') as fh:
        return [x.strip('\n') for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    list_map = read_input_lines()
    paths = set()
    letters = []

    portals = {} # loc -> loc
    portal_coords = defaultdict(list) # XX -> {loc1,loc2}

    for rownr in range(len(list_map)):
        for colnr in range(len(list_map[rownr])):
            loc = rownr+(1j*colnr)
            if list_map[rownr][colnr] == '.':
                paths.add(loc)
            if list_map[rownr][colnr].isupper():
                letters.append(loc)

    for loc in paths:
        for dir in {1, -1, 1j, -1j}:
            if (loc + dir) in letters and loc+(dir*2) in letters:

                if dir in {1,1j}:
                    l1, l2  =loc+dir, loc+2*dir
                else:
                    l1, l2 = loc+2*dir,loc+dir
                portal = list_map[int(l1.real)][int(l1.imag)] + list_map[int(l2.real)][int(l2.imag)]
                portal_coords[portal].append(loc )

    for portal in portal_coords:
        if portal not in {'AA','ZZ'}:
            a, b = portal_coords[portal]
            portals[a] = b
            portals[b] = a


    distdict = {portal_coords['AA'][0]:0}
    previous = set([portal_coords['AA'][0]])

    while previous:
        next = set()
        for pos in previous:
            for dir in {1,-1,1j,-1j}:
                if (pos+dir in paths) and (pos+dir) not in distdict:
                    next.add(pos+dir)
                    distdict[pos+dir] = distdict[pos]+1
            if pos in portals:
                if portals[pos] not in distdict:
                    distdict[portals[pos]] = distdict[pos] +1
                    next.add(portals[pos])

        previous = next

    print(distdict[portal_coords['ZZ'][0]])


def part_b(): # 7168 too big
    list_map = read_input_lines()#"input_dummy.txt")
    paths = set()
    letters = []

    portals = {}  # loc -> loc
    portal_coords = defaultdict(list)  # XX -> {loc1,loc2}

    for rownr in range(len(list_map)):
        for colnr in range(len(list_map[rownr])):
            loc = rownr + (1j * colnr)
            if list_map[rownr][colnr] == '.':
                paths.add(loc)
            if list_map[rownr][colnr].isupper():
                letters.append(loc)

    def isinner (loc):
        yrange = {x for x in range(3,len(list_map)-3)}
        xrange = {x for x in range(3,max([len(x) for x in list_map])-3)}
        return (int(loc.real) in yrange ) and (int(loc.imag) in xrange)

    for loc in paths:
        for dir in {1, -1, 1j, -1j}:
            if (loc + dir) in letters :
                assert loc+(dir*2) in letters
                if dir in {1,1j}:
                    l1, l2  =loc+dir, loc+2*dir
                else:
                    l1, l2 = loc+2*dir,loc+dir
                portal = list_map[int(l1.real)][int(l1.imag)] + list_map[int(l2.real)][int(l2.imag)]
                portal_coords[portal].append(loc )

    for portal in portal_coords:
        if portal not in {'AA', 'ZZ'}:
            a, b = portal_coords[portal]
            portals[a] = b
            portals[b] = a

    def get_all_non_portal_dists_from_loc(loc):
        distdict = {loc:0}
        previous = {loc,}
        while previous:
            next = set()
            for pos in previous:
                for dir in {1, -1, 1j, -1j}:
                    if ((pos + dir) in paths) and ((pos + dir) not in distdict):
                        next.add((pos + dir))
                        distdict[(pos + dir)] = distdict[pos] + 1
            previous = next
            #only return edges if they are relevant ( portals)
        return {k :distdict[k] for k in distdict if k in (set(portals) | {portal_coords['AA'][0],portal_coords['ZZ'][0]})}

    portaldict = {l: get_all_non_portal_dists_from_loc(l) for l in (set(portals) | {portal_coords['AA'][0],portal_coords['ZZ'][0]})}
    distdict = {}

    tiebreaker = [1]

    def get_next_moves(total_dist,new_loc):
        loc, level = new_loc
        new_dist_list = [(total_dist + portaldict[loc][x],(x,level))for x in portaldict[loc] if (x,level) not in distdict]

        if loc in portals:
            if isinner(loc):
                deltalevel = 1
            else:
                deltalevel = -1

            if (level + deltalevel) >= 0  and (portals[loc],level + deltalevel) not in distdict:
                new_dist_list.append((total_dist + 1,(portals[loc],level + deltalevel)))

        new_dist_list = [(new_dist_list[i][0],tiebreaker[0]+i,new_dist_list[i][1]) for i in range(len(new_dist_list))]
        tiebreaker[0] += len(new_dist_list)
        return new_dist_list

    heap =[(0,0,(portal_coords['ZZ'][0],0))]
    heapq.heapify(heap)

    while not ((portal_coords['AA'][0],0) in distdict):
        dist,_, next_loc = heapq.heappop(heap)
        if next_loc not in distdict:
            distdict[next_loc] = dist
            for new_move in get_next_moves(dist,next_loc):
                heapq.heappush(heap, new_move)

    print(distdict[(portal_coords['AA'][0],0)])

part_a()
part_b()




