<<<<<<< HEAD
#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[0].split(',')
    date = key[3][0:10]
    print "%s\t%s" % (date, l[1])
=======
#!/usr/bin/env python

import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    key = l[0].split(',')
    date = key[3][0:10]
    print "%s\t%s" % (date, l[1])
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
