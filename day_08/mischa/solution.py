from collections import defaultdict, Counter

data = open('day08_input.txt')
lines = data.readline().strip()
lines1  = [int(x) for x in lines]

'''
part 1
'''
width = 25
length = 6

def part_1(inp):
    inp_len = len(inp)
    lay_len = width*length
    num_lay = int(inp_len/lay_len)

    dict_of_lay = defaultdict(list)
    least_z = float('inf')
    lay_zero = ''

    for i in range(num_lay):
        start,end = i*lay_len,((i+1)*lay_len)
        chunk = inp[start:end]

        c = Counter(chunk)
        if c[0] < least_z:
            lay_zero = 'layer_'+str(i)
            least_z = c[0]
        dict_of_lay['layer_'+str(i)]= c
    return  dict_of_lay[lay_zero][2]*dict_of_lay[lay_zero][1]
print(part_1(lines1))


'''
part 2
'''
def get_color(pixel_list):
    for i in pixel_list:
        if i == 1:
            return '#'
        elif i == 0:
            return '_'

def part_2(inp):
    inp_len = len(inp)
    lay_len = width*length
    num_lay = int(inp_len/lay_len)
    dict_of_pixel = defaultdict(list)
    for i in range(num_lay):
        start,end = i*lay_len,((i+1)*lay_len)
        chunk = inp[start:end]
        for i in range(len(chunk)):
            dict_of_pixel[i].append(chunk[i])
    pixel_color = []
    for i in dict_of_pixel:
        pixel = dict_of_pixel[i]
        color = get_color(pixel)
        pixel_color.append(color)
    return  pixel_color

p_c = part_2(lines1)

for i in range(6):
    start, end = i * 25, ((i + 1) * 25)
    print(p_c[start:end])
