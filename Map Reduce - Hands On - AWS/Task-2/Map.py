import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    value = l[1].split(",")
    fareAmount = float(value[11])
    if 0 <= fareAmount <= 4.00:
        print "%i, %i\t%i" % (0, 4, 1)
    elif 4.01 <= fareAmount <= 8:
        print "%i, %i\t%i" % (4.01, 8, 1)
    elif 8.01 <= fareAmount <= 12:
        print "%i, %i\t%i" % (8.01, 12, 1)
    elif 12.01 <= fareAmount <= 16:
        print "%i, %i\t%i" % (12.01, 16, 1)
    elif 16.01 <= fareAmount <= 20:
        print "%i, %i\t%i" % (16.01, 20, 1)
    elif 20.01 <= fareAmount <= 24:
        print "%i, %i\t%i" % (20.01, 24, 1)
    elif 24.01 <= fareAmount <= 48:
        print "%i, %i\t%i" % (24.01, 48, 1)

    else:
        print "%i, %i\t%i" % (48.01, sys.maxint, 1)