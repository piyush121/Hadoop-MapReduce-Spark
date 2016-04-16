<<<<<<< HEAD
#!/usr/bin/env python

import sys

prevKey = ""
trips = 0
totalRev = 0.00
tip = 0.00

for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    line = line[1].split(",")
    fareAmount = float(line[0])
    currTip = float(line[1])
    if prevKey == "":
        prevKey = currKey
        trips += 1
        totalRev += fareAmount
        tip = currTip
        continue
    if currKey == prevKey:
        trips += 1
        totalRev += fareAmount
        tip += currTip
    else:
        print "%s\t%i,%.2f,%.2f" % (prevKey, trips, totalRev, (tip/trips) * 100)
        prevKey = currKey
        trips = 1
        tip = currTip
        totalRev = fareAmount
print "%s\t%i,%.2f,%.2f" % (prevKey, trips, totalRev, (tip/trips) * 100)


=======
#!/usr/bin/env python

import sys

prevKey = ""
trips = 0
totalRev = 0.00
tip = 0.00

for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    line = line[1].split(",")
    fareAmount = float(line[0])
    currTip = float(line[1])
    if prevKey == "":
        prevKey = currKey
        trips += 1
        totalRev += fareAmount
        tip = currTip
        continue
    if currKey == prevKey:
        trips += 1
        totalRev += fareAmount
        tip += currTip
    else:
        print "%s\t%i,%.2f,%.2f" % (prevKey, trips, totalRev, (tip/trips) * 100)
        prevKey = currKey
        trips = 1
        tip = currTip
        totalRev = fareAmount
print "%s\t%i,%.2f,%.2f" % (prevKey, trips, totalRev, (tip/trips) * 100)


>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
