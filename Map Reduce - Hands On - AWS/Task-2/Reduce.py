import sys
prevKey = ""
currKey = ""
totalSum = 0
for line in sys.stdin:
    line.strip().split("\t")
    currKey = line[0]
    if prevKey == "":
        currKey = prevKey
        totalSum += 1
        continue

    if currKey == prevKey:
        totalSum += 1
    else:
        print "prevKey\tsum"
        totalSum = 1
        prevKey = currKey
    print "prevKey\tsum"
