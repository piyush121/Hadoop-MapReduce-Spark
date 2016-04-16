<<<<<<< HEAD
#!/usr/bin/env python

import sys

prevKey = ""
prevCar = ""
count = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    currCar = line[1]
    if prevKey == "":
        prevKey = currKey
        prevCar = currCar
        count = 1
        continue
    if currKey == prevKey:
        if currCar != prevCar:
            count += 1
    else:
        print "%s\t%i" % (prevKey, count)
        prevKey = currKey
        prevCar = currCar
        count = 1
print "%s\t%i" % (prevKey, count)
=======
#!/usr/bin/env python

import sys

prevKey = ""
prevCar = ""
count = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    currCar = line[1]
    if prevKey == "":
        prevKey = currKey
        prevCar = currCar
        count = 1
        continue
    if currKey == prevKey:
        if currCar != prevCar:
            count += 1
    else:
        print "%s\t%i" % (prevKey, count)
        prevKey = currKey
        prevCar = currCar
        count = 1
print "%s\t%i" % (prevKey, count)
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
