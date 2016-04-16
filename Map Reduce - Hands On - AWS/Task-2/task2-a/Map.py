<<<<<<< HEAD
#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    value = l[1].split(",")
    fareAmount = float(value[11])
    if 0 <= fareAmount <= 4.00:
        print "%i,%i\t%i" % (0, 4, 1)
    elif 4.01 <= fareAmount <= 8:
        print "%.2f,%i\t%i" % (4.01, 8, 1)
    elif 8.01 <= fareAmount <= 12:
        print "%.2f,%i\t%i" % (8.01, 12, 1)
    elif 12.01 <= fareAmount <= 16:
        print "%.2f,%i\t%i" % (12.01, 16, 1)
    elif 16.01 <= fareAmount <= 20:
        print "%.2f,%i\t%i" % (16.01, 20, 1)
    elif 20.01 <= fareAmount <= 24:
        print "%.2f,%i\t%i" % (20.01, 24, 1)
    elif 24.01 <= fareAmount <= 28:
        print "%.2f,%i\t%i" % (24.01, 28, 1)
    elif 28.01 <= fareAmount <= 32:
        print "%.2f,%i\t%i" % (28.01, 32, 1)
    elif 32.01 <= fareAmount <= 36:
        print "%.2f,%i\t%i" % (32.01, 36, 1)
    elif 36.01 <= fareAmount <= 40:
        print "%.2f,%i\t%i" % (36.01, 40, 1)
    elif 40.01 <= fareAmount <= 44:
        print "%.2f,%i\t%i" % (40.01, 44, 1)
    elif 44.01 <= fareAmount <= 48:
        print "%.2f,%i\t%i" % (44.01, 48, 1)
    else:
=======
#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    value = l[1].split(",")
    fareAmount = float(value[11])
    if 0 <= fareAmount <= 4.00:
        print "%i,%i\t%i" % (0, 4, 1)
    elif 4.01 <= fareAmount <= 8:
        print "%.2f,%i\t%i" % (4.01, 8, 1)
    elif 8.01 <= fareAmount <= 12:
        print "%.2f,%i\t%i" % (8.01, 12, 1)
    elif 12.01 <= fareAmount <= 16:
        print "%.2f,%i\t%i" % (12.01, 16, 1)
    elif 16.01 <= fareAmount <= 20:
        print "%.2f,%i\t%i" % (16.01, 20, 1)
    elif 20.01 <= fareAmount <= 24:
        print "%.2f,%i\t%i" % (20.01, 24, 1)
    elif 24.01 <= fareAmount <= 28:
        print "%.2f,%i\t%i" % (24.01, 28, 1)
    elif 28.01 <= fareAmount <= 32:
        print "%.2f,%i\t%i" % (28.01, 32, 1)
    elif 32.01 <= fareAmount <= 36:
        print "%.2f,%i\t%i" % (32.01, 36, 1)
    elif 36.01 <= fareAmount <= 40:
        print "%.2f,%i\t%i" % (36.01, 40, 1)
    elif 40.01 <= fareAmount <= 44:
        print "%.2f,%i\t%i" % (40.01, 44, 1)
    elif 44.01 <= fareAmount <= 48:
        print "%.2f,%i\t%i" % (44.01, 48, 1)
    else:
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
        print "%.2f,%s\t%i" % (48.01, "infinite", 1)