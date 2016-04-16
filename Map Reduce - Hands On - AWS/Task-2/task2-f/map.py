<<<<<<< HEAD
#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split("\t")[0].split(",")
    hackLicense = line[1]
    medallion = line[0]
    print "%s\t%s" % (hackLicense, medallion)
=======
#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split("\t")[0].split(",")
    hackLicense = line[1]
    medallion = line[0]
    print "%s\t%s" % (hackLicense, medallion)
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
