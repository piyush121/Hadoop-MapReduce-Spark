import StringIO
import csv
import sys


for line in sys.stdin:
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        if 'MEDALLION' == record[2]:
            key = record[0]
            rem = ",".join(record[1:])
            print "%s\t%s%s" % (key, '1', rem)
        else:
            key = record[0]
            rem = ",".join(record[1:]).replace("\t", ",")
            print "%s\t%s%s" % (key, '0', rem)
