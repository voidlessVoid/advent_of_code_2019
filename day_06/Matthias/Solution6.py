orbiters = []
centers = []

total_orbits = 0

with open("input6.txt") as f:
    lines = f.readlines()
    for line in lines:
        center = "%s%s%s" % (line[0], line[1], line[2])
        centers.append(center)
        orbiter = "%s%s%s" % (line[4], line[5], line[6])
        orbiters.append(orbiter)

while len(orbiters) > 0:
    for item in orbiters:
        if item in centers:
            total_orbits += 1
            print item
        else:
            orbiters.remove(item)
            print item
            

print total_orbits
