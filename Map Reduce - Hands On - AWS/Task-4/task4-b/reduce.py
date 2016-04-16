<<<<<<< HEAD
#!/usr/bin/env python

import sys

import operator
prevKey = ""
totalRev = 0.00
count = {'None': 0.00}

for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    revenue = float(line[1])
    if prevKey == "":
        prevKey = currKey
        totalRev += revenue
        continue
    if currKey == prevKey:
        totalRev += revenue
    else:
        count[prevKey] = totalRev
        prevKey = currKey
        totalRev = revenue
count[prevKey] = totalRev

for i in range(0, 20):
    tpword = max(count.iteritems(), key=operator.itemgetter(1))[0]
    if tpword != "None":
        print "%s\t%.2f" % (tpword, count[tpword])
    count[tpword] = 0.00
=======
#!/usr/bin/env python

import sys

import operator
prevKey = ""
totalRev = 0.00
count = {'None': 0.00}

for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    revenue = float(line[1])
    if prevKey == "":
        prevKey = currKey
        totalRev += revenue
        continue
    if currKey == prevKey:
        totalRev += revenue
    else:
        count[prevKey] = totalRev
        prevKey = currKey
        totalRev = revenue
count[prevKey] = totalRev

for i in range(0, 20):
    tpword = max(count.iteritems(), key=operator.itemgetter(1))[0]
    if tpword != "None":
        print "%s\t%.2f" % (tpword, count[tpword])
    count[tpword] = 0.00
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
