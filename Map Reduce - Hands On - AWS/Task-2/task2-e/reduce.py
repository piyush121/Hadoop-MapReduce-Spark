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
    if prevKey == currKey:
        if currDay == prevDay:
            days += 1
        trips += 1
    else:
        print "%s\t%i,%i" % (prevKey, trips, trips / days)
        prevKey = currKey
        trips = 1
        days = 1
print "%s\t%i,%i" % (prevKey, trips, trips / days)
