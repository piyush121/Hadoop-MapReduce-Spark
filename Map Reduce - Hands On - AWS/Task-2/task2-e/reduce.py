<<<<<<< HEAD
#!/usr/bin/env python

import sys

prevKey = ""
prevDay = ""
trips = 0
days = 0
for line in sys.stdin:
    line = line.split("\t")
    currKey = line[0]
    currDay = line[1][0:10]
    if prevKey == "":
        prevKey = currKey
        prevDay = currDay
        trips = 1
        days = 1
        continue
    if currKey == prevKey:
        if currDay != prevDay:
            days += 1
        trips += 1
    else:
        print "%s\t%i,%.2f" % (prevKey, trips, float(trips / days))
        prevKey = currKey
        prevDay = currDay
        trips = 1
        days = 1
print "%s\t%i,%.2f" % (prevKey, trips, float(trips / days))
=======
#!/usr/bin/env python

import sys

prevKey = ""
prevDay = ""
trips = 0
days = 0
for line in sys.stdin:
    line = line.split("\t")
    currKey = line[0]
    currDay = line[1][0:10]
    if prevKey == "":
        prevKey = currKey
        prevDay = currDay
        trips = 1
        days = 1
        continue
    if currKey == prevKey:
        if currDay != prevDay:
            days += 1
        trips += 1
    else:
        print "%s\t%i,%.2f" % (prevKey, trips, float(trips / days))
        prevKey = currKey
        prevDay = currDay
        trips = 1
        days = 1
print "%s\t%i,%.2f" % (prevKey, trips, float(trips / days))
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
