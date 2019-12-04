from collections import defaultdict
data = open('day03_input.txt')
path_data = data.readlines()

path_data1 = path_data[0].split(',')
path_data2 = path_data[1].split(',')

'''
puts every touched coordinate for one wire in a set and a list (omg)...
'''
def make_path(inp):
    path_coords = set()
    path_coord_list = []
    x,y = 0,0
    for i in range(len(inp)):
        direction = inp[i][0]
        steps = int(inp[i][1:])
        steps_total = 0
        steps_to_collision = defaultdict
        if direction == 'R':
            for i in range(steps):
                x +=1
                last_stop = (x,y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)

        elif direction == 'L':
            for i in range(steps):
                x -=1
                last_stop = (x,y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)
        elif direction == 'U':
            for i in range(steps):
                y +=1
                last_stop = (x,y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)
        elif direction == 'D':
            for i in range(steps):
                y -=1
                last_stop = (x,y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)
        steps_total += 1
    return path_coords,path_coord_list
'''
takes the collisions from part 1 and counts the steps for 1 wire until it reaches every collision point
'''
def make_path_steps(inp, collisions):
    path_coords = set()
    path_coord_list = []
    x, y = 0, 0
    steps_total =0
    steps_to_collision = defaultdict(int)
    for i in range(len(inp)):
        direction = inp[i][0]
        steps = int(inp[i][1:])

        if direction == 'R':
            for i in range(steps):
                steps_total += 1
                x += 1
                last_stop = (x, y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)
                if last_stop in collisions:
                    steps_to_collision[last_stop] = steps_total
        elif direction == 'L':
            for i in range(steps):
                steps_total += 1
                x -= 1
                last_stop = (x, y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)
                if path_coord_list[-1] in collisions:
                    steps_to_collision[path_coord_list[-1]]=steps_total
        elif direction == 'U':
            for i in range(steps):
                steps_total += 1
                y += 1
                last_stop = (x, y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)
                if path_coord_list[-1] in collisions:
                    steps_to_collision[path_coord_list[-1]] = steps_total
        elif direction == 'D':
            for i in range(steps):
                steps_total += 1
                y -= 1
                last_stop = (x, y)
                path_coords.add(last_stop)
                path_coord_list.append(last_stop)
                if path_coord_list[-1] in collisions:
                    steps_to_collision[path_coord_list[-1]] = steps_total
    return  steps_to_collision

'''
gets manhattan distance from (0,0) for a given list of coords and returns the minimum
'''
def get_distance(inp):
    distances = []
    for i in inp:
        dist = abs(i[0]-0)+abs(i[1]-0)
        distances.append(dist)
    return min(distances)


'''
part 1
'''
path1,p_list1 = make_path(path_data1)
path2,p_list2 = make_path(path_data2)
collisions = path1.intersection(path2)
print(get_distance(collisions))
# 3229

'''
part 2
'''
collsion_steps1 = make_path_steps(path_data1,collisions)
collsion_steps2 = make_path_steps(path_data2,collisions)
steps_to_collisions = []
for i in collsion_steps1:
    steps1 = collsion_steps1[i]
    steps2 = collsion_steps2[i]
    combined_steps = steps1+steps2
    steps_to_collisions.append(combined_steps)
print(min(steps_to_collisions))
#32132
