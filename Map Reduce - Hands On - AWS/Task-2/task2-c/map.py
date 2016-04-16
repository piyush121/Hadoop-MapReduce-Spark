#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[1].split(',')
    key = int(key[3])
    print "%i\t" % key
