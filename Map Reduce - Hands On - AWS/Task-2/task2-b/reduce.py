#!/usr/bin/env python

import sys
count = 0
for line in sys.stdin:
    l = line.strip().split("\t")
    totalAmount = float(l[0])
    if totalAmount <= 10:
        count += 1
print count
