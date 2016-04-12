import sys
for line in sys.stdin:

    l = line.strip().split(",")
    if l[0] == 'medallion':
        continue
    if len(l) == 14:
        print "%s,%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (
            l[0], l[1], l[2], l[5], 0, l[3], l[4], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13])
    if len(l) == 11:
        print "%s,%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s" % (
            l[0], l[1], l[2], l[3], 1, l[4], l[5], l[6], l[7], l[8], l[9], l[10])
