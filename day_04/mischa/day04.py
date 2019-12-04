import re
#input: 284639-748759
a = 284639
b = 748759

def part_a(a, b):
    s = set()
    for i in range(a,b,1):
        if len(set(str(i))) < len(str(i)) and '1' not in str(i) and '0' not in str(i):
            if re.search(r'(([0-9])\2)',str(i)):
                last_digit,add = 2, True
                for x in str(i):
                    if int(x) < last_digit:
                        add = False
                    last_digit = int(x)
                if add == True:
                    s.add(i)
    return len(s)


def part_b(a,b):
    s = set()
    for i in range(a, b, 1):
        if len(set(str(i))) < len(str(i)) and '1' not in str(i) and '0' not in str(i):
            q = re.findall(r'(([0-90-9])\2)', str(i))
            if q:
                last_digit,add = 2, True
                w = re.findall(r'(([0-90-9])\2+)', str(i))
                if q==w:
                    for x in str(i):
                        if int(x) < last_digit:
                            add = False
                        last_digit = int(x)
                    if add == True:
                        s.add(i)
                elif len(w)>1:
                    if len(w[0][0]) != len(w[1][0]):
                        for x in str(i):
                            if int(x) < last_digit:
                                add = False
                            last_digit = int(x)
                        if add == True:
                            s.add(i)
    return len(s)
print(part_a(a,b))
#895

print(part_b(a,b))
#591