import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines(inp = 'input.txt'):
    with open(inp, 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    list_map = read_input_lines()
    paths = set()
    doors = {} # loc -> letter
    keys = {} # letter -> loc

    for row in range(len(list_map)):
        for col in range(len(list_map[row])):
            loc = row+(col*1j)
            if list_map[row][col] != '#':
                paths.add(loc)
            if list_map[row][col].islower():
                keys[list_map[row][col]] = loc
            if list_map[row][col].isupper():
                doors[loc] = list_map[row][col]
            if list_map[row][col] == '@':
                iloc = loc

    def get_dists_from_loc(loc):
        dists = {loc:(0,tuple())}
        last_visited = {loc}
        while last_visited:
            new_last_visited = set()
            for loc in last_visited:
                for dir in {1, -1, 1j, -1j}:
                    if ((loc+dir) in paths) and not ((loc+dir) in dists):
                        new_last_visited.add(loc+dir)
                        new_dist = dists[loc][0]+1
                        req_keys =  dists[loc][1]
                        if loc in doors:
                            req_keys += (doors[loc].lower(),)
                        dists[loc+dir] =(new_dist,req_keys)
            last_visited = new_last_visited
        return dists

    dist_to_dist_dict = {k:get_dists_from_loc(k) for k in paths} #brute force FTW
    print('calculated state dists')


    def get_possible_future_states(state):
        state_location, collected_keys = state
        output = {}
        for key in set(keys) - set(collected_keys):
            dist_to_key, keys_required = dist_to_dist_dict[state_location][keys[key]]  # dist, keys required
            if all((k in collected_keys) for k in keys_required):  # we have all keys to go there
                cumulative_dist = dist_to_key + states[state]
                new_state_loc = keys[key]
                new_collected_keys = tuple(sorted(collected_keys + (key,)))
                output[(new_state_loc,new_collected_keys)] = cumulative_dist
        return output

    states = {(iloc,tuple()):0}
    future_states = get_possible_future_states((iloc,tuple()))
    while True:
        next_state = min(future_states, key=lambda x: future_states[x])
        states[next_state] = future_states[next_state]
        del future_states[next_state]
        new_future_states = get_possible_future_states(next_state)
        for new_future_state in new_future_states:
            if not new_future_state in states:
                if new_future_state in future_states:
                    future_states[new_future_state] = min([future_states[new_future_state],new_future_states[new_future_state]])
                else:
                    future_states[new_future_state] = new_future_states[new_future_state]
        if not(set(keys) - set(next_state[1])):
            print(states[next_state])
            break



def part_b(): # takes about 1h to run
    list_map = read_input_lines(inp = 'input2.txt')
    paths = set()
    doors = {}  # loc -> letter
    keys = {}  # letter -> loc
    locations = []

    for row in range(len(list_map)):
        for col in range(len(list_map[row])):
            loc = row + (col * 1j)
            if list_map[row][col] != '#':
                paths.add(loc)
            if list_map[row][col].islower():
                keys[list_map[row][col]] = loc
            if list_map[row][col].isupper():
                doors[loc] = list_map[row][col]
            if list_map[row][col] == '@':
                locations.append(loc)


    def get_dists_from_loc(loc):
        dists = {loc: (0, tuple())}
        last_visited = {loc}
        while last_visited:
            new_last_visited = set()
            for loc in last_visited:
                for dir in {1, -1, 1j, -1j}:
                    if ((loc + dir) in paths) and not ((loc + dir) in dists):
                        new_last_visited.add(loc + dir)
                        new_dist = dists[loc][0] + 1
                        req_keys = dists[loc][1]
                        if loc in doors:
                            req_keys += (doors[loc].lower(),)
                        dists[loc + dir] = (new_dist, req_keys)
            last_visited = new_last_visited
        return dists

    dist_to_dist_dict = {k: get_dists_from_loc(k) for k in paths}  # brute force FTW
    print('calculated state dists')

    def get_possible_future_states(state):
        state_locations, collected_keys = state
        output = {}
        for bot_index in range(len(state_locations)):
            for key in set(keys) - set(collected_keys):
                if keys[key] in dist_to_dist_dict[state_locations[bot_index]]: # if not in the right quadrant, cannot reach
                    dist_to_key, keys_required = dist_to_dist_dict[state_locations[bot_index]][keys[key]]  # dist, keys required
                    if all((k in collected_keys) for k in keys_required):  # we have all keys to go there
                        cumulative_dist = dist_to_key + states[state]
                        new_state_locations = state_locations[:bot_index] +(keys[key],) + state_locations[bot_index+1:]
                        new_collected_keys = tuple(sorted(collected_keys + (key,)))
                        output[(new_state_locations, new_collected_keys)] = cumulative_dist
        return output

    states = {(tuple(locations), tuple()): 0} # is a tuple of robot locations plus a tuple of fetched keys
    future_states = get_possible_future_states((tuple(locations), tuple()))
    while True:
        next_state = min(future_states, key=lambda x: future_states[x])
        states[next_state] = future_states[next_state]
        del future_states[next_state]
        new_future_states = get_possible_future_states(next_state)
        for new_future_state in new_future_states:
            if not new_future_state in states:
                if new_future_state in future_states:
                    future_states[new_future_state] = min(
                        [future_states[new_future_state], new_future_states[new_future_state]])
                else:
                    future_states[new_future_state] = new_future_states[new_future_state]
        if not (set(keys) - set(next_state[1])):
            print(states[next_state])
            break

part_b()