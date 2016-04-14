import sys

for line in sys.stdin:
    line = line.strip().split("\t")[0].split(",")
    medallion = line[0]
    day = line[3]
    print "%s\t%s" % (medallion, day)
