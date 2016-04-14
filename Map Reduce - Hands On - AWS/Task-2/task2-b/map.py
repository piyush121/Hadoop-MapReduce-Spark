import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[15]
    print "%.2f\t" % key
