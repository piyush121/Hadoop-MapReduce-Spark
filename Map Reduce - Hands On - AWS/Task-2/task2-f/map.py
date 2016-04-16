#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split("\t")[0].split(",")
    hackLicense = line[1]
    medallion = line[0]
    print "%s\t%s" % (hackLicense, medallion)
