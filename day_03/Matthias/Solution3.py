import sys

wire1 = []
wire2 = []

with open("Input3.txt") as f:
    lines = f.read().split("\n")
    wire1.append(lines[0].split(","))
    wire1 = wire1[0]
    wire2.append(lines[1].split(","))
    wire2 = wire2[0]

path_of_wire1 = []
path_of_wire2 = []
current_x = 0
current_y = 0

for element in wire1:
    if element[0] == "R":
        number = int(element.replace("R",""))
        for x in range(number):
            path_of_wire1.append((current_x+x+1,current_y))
        current_x += number
    elif element[0] == "L":
        number = int(element.replace("L",""))
        for x in range(number):
            path_of_wire1.append((current_x-x-1,current_y))
        current_x -= number
    elif element[0] == "U":
        number = int(element.replace("U",""))
        for y in range(number):
            path_of_wire1.append((current_x,current_y+y+1))
        current_y += number
    elif element[0] == "D":
        number = int(element.replace("D",""))
        for y in range(number):
            path_of_wire1.append((current_x,current_y-y-1))
        current_y -= number
    else:
        print "error"
        sys.exit()

for element in wire2:
    if element[0] == "R":
        number = int(element.replace("R",""))
        for x in range(number):
            path_of_wire2.append((current_x+x+1,current_y))
        current_x += number
    elif element[0] == "L":
        number = int(element.replace("L",""))
        for x in range(number):
            path_of_wire2.append((current_x-x-1,current_y))
        current_x -= number
    elif element[0] == "U":
        number = int(element.replace("U",""))
        for y in range(number):
            path_of_wire2.append((current_x,current_y+y+1))
        current_y += number
    elif element[0] == "D":
        number = int(element.replace("D",""))
        for y in range(number):
            path_of_wire2.append((current_x,current_y-y-1))
        current_y -= number
    else:
        print "error"
        sys.exit()

crossings = []
for element in path_of_wire1:
    print element
    if element in path_of_wire2:
        crossings.append(element)
print crossings

distances = []
for element in crossings:
    distance = abs(int(element[0])) + abs(int(element[1]))
    distances.append(distance)

distances.sort()
print distances
