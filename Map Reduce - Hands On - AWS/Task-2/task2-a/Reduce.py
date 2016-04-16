<<<<<<< HEAD
#!/usr/bin/env python

import sys
prevKey = ""
totalSum = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    if prevKey == "":
        prevKey = currKey
        totalSum += 1
        continue

    if currKey == prevKey:
        totalSum += 1
    else:
        print "%s\t%i" % (prevKey, totalSum)
        totalSum = 1
        prevKey = currKey
=======
#!/usr/bin/env python

import sys
prevKey = ""
totalSum = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0]
    if prevKey == "":
        prevKey = currKey
        totalSum += 1
        continue

    if currKey == prevKey:
        totalSum += 1
    else:
        print "%s\t%i" % (prevKey, totalSum)
        totalSum = 1
        prevKey = currKey
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
print "%s\t%i" % (prevKey, totalSum)