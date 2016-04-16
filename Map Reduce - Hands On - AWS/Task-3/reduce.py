#!/usr/bin/env python

import sys

prevKey = ""
currKey = ""
values1 = []
values2 = []
for line in sys.stdin:
    l = line.strip().split("\t")
    if len(prevKey) == 0:  # initial setup.
        prevKey = l[0]
        if l[1][0] == '0':
            values1.append(l[1][1:])
        if l[1][0] == '1':
            values2.append(l[1][1:])
        continue
    currKey = l[0]
    if currKey == prevKey:  # same key means we have to join them.
        if l[1][0] == '0':
            values1.append(l[1][1:])
        elif l[1][0] == '1':
            values2.append(l[1][1:])
        continue
    elif len(values2) > 0 and len(values1) > 0:  # values from both table should be present in order to join them.
        for value1 in values1:
            for value2 in values2:
                print '%s\t%s,%s' % (prevKey, value1, value2)

    prevKey = currKey  # new key arrives. Initialize again.
    values1 = []
    values2 = []
    if l[1][0] == '0':
        values1.append(l[1][1:])
    if l[1][0] == '1':
        values2.append(l[1][1:])

if len(values2) > 0 and len(values1) > 0:  # Finishing up.
    for value1 in values1:
        for value2 in values2:
            print '%s\t%s,%s' % (prevKey, value1, value2)
