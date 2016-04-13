import sys
prevKey = ""
currKey = ""
totalSum = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    currKey = line[0].strip()
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
