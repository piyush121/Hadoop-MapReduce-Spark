<<<<<<< HEAD
#!/usr/bin/env python

import sys
count = 0
for line in sys.stdin:
    l = line.strip().split("\t")
    totalAmount = float(l[0])
    if totalAmount <= 10:
        count += 1
print count
=======
#!/usr/bin/env python

import sys
count = 0
for line in sys.stdin:
    l = line.strip().split("\t")
    totalAmount = float(l[0])
    if totalAmount <= 10:
        count += 1
print count
>>>>>>> de414a49d2480963429fdff625f069d643fa27e4
