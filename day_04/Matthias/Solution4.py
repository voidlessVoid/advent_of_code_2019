counter = 0
for i in range(136818, 685979):
    string = str(i)
    lst = []
    for char in string:
        lst.append(char)
    
    if int(lst[5]) >= int(lst[4]) and int(lst[4]) >= int(lst[3]) and int(lst[3]) >= int(lst[2]) and int(lst[2]) >= int(lst[1]) and int(lst[1]) >= int(lst[0]):
        condition1 = 1
    else:
        condition1 = 0
    
    condition2 = 0
    if int(lst[0]) == int(lst[1]):
        if int(lst[0]) == int(lst[2]):
            condition2 += 0
        else:
            condition2 += 1
    elif int(lst[1]) == int(lst[2]):
        if int(lst[2]) == int(lst[3]) or int(lst[1]) == int(lst[0]):
            condition2 += 0
        else:
            condition2 += 1
    elif int(lst[2]) == int(lst[3]):
        if int(lst[3]) == int(lst[4]) or int(lst[2]) == int(lst[1]):
            condition2 += 0
        else:
            condition2 += 1
    elif int(lst[3]) == int(lst[4]):
        if int(lst[4]) == int(lst[5]) or int(lst[3]) == int(lst[2]):
            condition2 += 0
        else:
            condition2 += 1
    elif int(lst[4]) == int(lst[5]):
        if int(lst[4]) == int(lst[3]):
            condition2 += 0
        else:
            condition2 += 1
    else:
        condition2 += 0
    # Compute product. If any of the two conditions is zero, the counter won't go up.
    product = condition1 * condition2
    if product >= 1:
        counter += 1
print counter
