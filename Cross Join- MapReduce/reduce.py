#!/usr/bin/python

import sys


#input comes from STDIN (stream data that goes to the program)
courseNumber=None
courseName=None
for line in sys.stdin:
	key, index, name =line.strip().split("\t",2)
	identity=None
	try:
		identity=key[1]
	except ValueError:
		continue
	
	if identity=="C":
		courseNumber=index
		courseName=name
	else: 
		print "%s\t%s\t%s\t%s" %(index,name,courseNumber,courseName)
	#Fill in your reduce code here. To write to output file, use "print"

