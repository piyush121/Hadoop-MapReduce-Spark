#!/usr/bin/env python

import sys
prevKey = -1
currKey = -1
count = 0
for line in sys.stdin:
    l = line.strip().split("\t")
    currKey = int(l[0])
    if prevKey == -1:
        prevKey = currKey
        count += 1
        continue
    if currKey == prevKey:
        count += 1
    else:
        print "%i\t%i" % (prevKey, count)
        prevKey = currKey
        count = 1
print "%i\t%i" % (prevKey, count)
