#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[1].split(',')
    key = key[16]
    print "%.2f\t" %float(key)
