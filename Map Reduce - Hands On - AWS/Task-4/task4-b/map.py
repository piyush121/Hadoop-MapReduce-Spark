<<<<<<< HEAD
#!/usr/bin/env python

import StringIO
import csv
import sys


for record in sys.stdin:
    csv_file = StringIO.StringIO(record)
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        key = line[29]
        revenue = float(line[14]) + float(line[15]) + float(line[17])
        print "%s\t%f" % (key, revenue)
=======
#!/usr/bin/env python

import StringIO
import csv
import sys


for record in sys.stdin:
    csv_file = StringIO.StringIO(record)
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        key = line[29]
        revenue = float(line[14]) + float(line[15]) + float(line[17])
        print "%s\t%f" % (key, revenue)
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
