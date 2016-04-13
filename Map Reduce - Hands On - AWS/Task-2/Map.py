import sys

for line in sys.stdin:
    line = line.strip().split("\t")
    line = line.split(",")
    fareAmount = line[9]

    if 0 <= fareAmount <= 4:
        print "%i, %i\t%i" % (0, 4, 1)
    if 4.01 <= fareAmount <= 8:
        print "%i, %i\t%i" % (4.01, 8, 1)
    if 8.01 <= fareAmount <= 12:
        print "%i ,%i\t%i" % (8.01, 12, 1)
    if 12.01 <= fareAmount <= 16:
        print "%i, %i\t%i" % (12.01, 16, 1)
    if 16.01 <= fareAmount <= 20:
        print "%i, %i\t%i" % (16.01, 20, 1)
    if 20.01 <= fareAmount <= 14:
        print "%i, %i\t%i" % (20.01, 24, 1)
    if 24.01 <= fareAmount <= 48:
        print "%i, %i\t%i" % (24.01, 48, 1)

    if 0 <= fareAmount <= sys.maxint:
        print "%i, infinite\t%i" % (0, 1)