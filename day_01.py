file_object = open('day_1_input.txt')
lines = file_object.readlines()

def freq(lines):
    frequency = 0
    totals = set([0])

    while True:
        for i in lines:
            a = i.strip()
            frequency = frequency + int(a)
            if frequency in totals:
                return 'first freq twice:' + str(frequency) + 'length: ' + str(len(totals))

            else:
                totals.add(frequency)

print(freq(lines))
