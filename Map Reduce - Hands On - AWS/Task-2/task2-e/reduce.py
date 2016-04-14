import sys

prevKey = ""
prevDay = ""
trips = 0
days = 0
for line in sys.stdin:
    line = line.split("\t")
    currKey = line[0]
    currDay = line[1][0:10]
    if prevKey == "":
        prevKey = currKey
        prevDay = currDay
        trips = 1
        days = 1
        continue
    if currKey == prevKey:
        if currDay != prevDay:
            days += 1
        trips += 1
    else:
        print "%s\t%i,%.2f" % (prevKey, trips, float(trips / days))
        prevKey = currKey
        prevDay = currDay
        trips = 1
        days = 1
print "%s\t%i,%.2f" % (prevKey, trips, float(trips / days))
