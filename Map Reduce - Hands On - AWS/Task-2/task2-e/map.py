<<<<<<< HEAD
#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split("\t")[0].split(",")
    medallion = line[0]
    day = line[3]
    print "%s\t%s" % (medallion, day)
=======
#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split("\t")[0].split(",")
    medallion = line[0]
    day = line[3]
    print "%s\t%s" % (medallion, day)
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
