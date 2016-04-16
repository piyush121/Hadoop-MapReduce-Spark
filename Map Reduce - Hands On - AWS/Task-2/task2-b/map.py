<<<<<<< HEAD
#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[1].split(',')
    key = key[16]
    print "%.2f\t" %float(key)
=======
#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[1].split(',')
    key = key[16]
    print "%.2f\t" %float(key)
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
