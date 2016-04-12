import sys

prevKey = ""
currKey = ""
values1 = []
values2 = []
for line in sys.stdin:
    l = line.strip().split("\t")
    if len(prevKey) == 0:
        prevKey = l[0]
        if l[1][0] == '0':
            values1.append(l[1][2:])
        if l[1][0] == '1':
            values2.append(l[1][2:])
        continue
    currKey = l[0]
    if currKey == prevKey:
        if l[1][0] == '0':
            values1.append(l[1][2:])
        elif l[1][0] == '1':
            values2.append(l[1][2:])
        continue
    elif len(values2) > 0 and len(values1) > 0:
        for value1 in values1:
            for value2 in values2:
                print "%s\t%s,%s" % (prevKey, value1, value2)

    prevKey = currKey
    values1 = []
    values2 = []
    if l[1][0] == '0':
        values1.append(l[1][2:])
    if l[1][0] == '1':
        values2.append(l[1][2:])

if len(values2) > 0 and len(values1) > 0:
    for value1 in values1:
        for value2 in values2:
            print "%s\t%s,%s" % (prevKey, value1, value2)
