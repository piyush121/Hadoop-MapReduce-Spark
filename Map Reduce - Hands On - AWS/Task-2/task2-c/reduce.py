<<<<<<< HEAD
#!/usr/bin/env python

import sys
prevKey = -1
currKey = -1
count = 0
for line in sys.stdin:
    l = line.strip().split("\t")
    currKey = int(l[0])
    if prevKey == -1:
        prevKey = currKey
        count += 1
        continue
    if currKey == prevKey:
        count += 1
    else:
        print "%i\t%i" % (prevKey, count)
        prevKey = currKey
        count = 1
print "%i\t%i" % (prevKey, count)
=======
#!/usr/bin/env python

import sys
prevKey = -1
currKey = -1
count = 0
for line in sys.stdin:
    l = line.strip().split("\t")
    currKey = int(l[0])
    if prevKey == -1:
        prevKey = currKey
        count += 1
        continue
    if currKey == prevKey:
        count += 1
    else:
        print "%i\t%i" % (prevKey, count)
        prevKey = currKey
        count = 1
print "%i\t%i" % (prevKey, count)
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
