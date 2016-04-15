#!/usr/bin/env python

import StringIO
import csv
import sys


for line in sys.stdin:
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        if record[2] == "MEDALLION":
            key = record[0]
            if line.split(",")[1][0] == "\"":
                name = "\""+record[1]+"\""
            else:
                name = record[1]
            rem = ",".join(record[2:])
            print '%s\t%s%s,%s' % (key, '1', name, rem)
        else:
            key = record[0]
            rem = ",".join(record[1:]).replace("\t", ",")
            print '%s\t%s%s' % (key, '0', rem)
