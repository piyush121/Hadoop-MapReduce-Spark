import sys

for line in sys.stdin:

    line = line.strip()

    if len(line) == 263:
        line = line.split("\t")
        left = line[0].split(",")
        key = left[0]
        leftr = "".join(left[1:])
        print "%s\t%s,%s" % (key, leftr, line[1])
    elif len(line) == 185:
        line = line.split(",")
        key = line[0]
        rem = "".join(line[1:])
        print "%s\t%s" % (key, rem)
