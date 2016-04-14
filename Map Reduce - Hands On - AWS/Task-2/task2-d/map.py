import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[0].split(',')
    date = key[3][0:10]
    print "%s\t%s" % (date, l[1])
