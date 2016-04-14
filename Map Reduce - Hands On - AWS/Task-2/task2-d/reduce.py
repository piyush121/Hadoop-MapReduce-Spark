import sys
prevKey = ""
currKey = ""
fareAmount = 0.0
tips = 0.0
surcharge = 0.00
tolls = 0.00
for line in sys.stdin:
    l = line.strip().split("\t")
    values = l[1].split(",")
    currKey = l[0]
    currFareAmount = float(values[11])
    currSurcharge = float(values[12])
    currTips = float(values[14])
    currToll = float(values[15])
    if prevKey == "":
        prevKey = currKey
        fareAmount += currFareAmount
        surcharge += currSurcharge
        tips += currTips
        tolls += currToll
        continue
    if currKey == prevKey:
        fareAmount += currFareAmount
        surcharge += currSurcharge
        tips += currTips
        tolls += currToll
    else:
        print "%s\t%.2f,%.2f" % (prevKey, fareAmount + surcharge + tips, currToll)
        prevKey = currKey
        fareAmount = currFareAmount
        surcharge = currSurcharge
        tips = currTips
        tolls = currToll
print "%s\t%.2f,%.2f" % (prevKey, fareAmount + surcharge + tips, currToll)
