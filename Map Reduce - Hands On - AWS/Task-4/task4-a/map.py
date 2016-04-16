<<<<<<< HEAD
#!/usr/bin/env python

import StringIO
import csv
import sys


for record in sys.stdin:
    csv_file = StringIO.StringIO(record)
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        key = line[25]
        revenue = float(line[14]) + float(line[15]) + float(line[17])
        tip = float(line[17])
        if revenue == 0:
			print "%s\t%f,%f" % (key, revenue, 0.00)
        else:
			print "%s\t%f,%f" % (key, revenue, tip/revenue)
=======
#!/usr/bin/env python

import StringIO
import csv
import sys


for record in sys.stdin:
    csv_file = StringIO.StringIO(record)
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        key = line[25]
        revenue = float(line[14]) + float(line[15]) + float(line[17])
        tip = float(line[17])
        if revenue == 0:
			print "%s\t%f,%f" % (key, revenue, 0.00)
        else:
			print "%s\t%f,%f" % (key, revenue, tip/revenue)
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
