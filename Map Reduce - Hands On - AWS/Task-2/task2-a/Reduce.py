#!/usr/bin/env python

import sys
prevKey = ""
totalSum = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    if prevKey == "":
        prevKey = currKey
        totalSum += 1
        continue

    if currKey == prevKey:
        totalSum += 1
    else:
        print "%s\t%i" % (prevKey, totalSum)
        totalSum = 1
        prevKey = currKey
print "%s\t%i" % (prevKey, totalSum)