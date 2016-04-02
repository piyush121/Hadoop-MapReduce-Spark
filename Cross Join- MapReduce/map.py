#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
courseCount=0
totalProfessorCount=0
totalCourseCount=0
lineCount=0
fixedCounter=1
variableCounter=0

for line in sys.stdin:
	l = line.strip().split()
	if int(l[0])==1:
		totalProfessorCount=totalProfessorCount+1
	else:
		totalCourseCount=totalCourseCount+1
totalLines=totalProfessorCount*totalCourseCount
while lineCount<totalLines:
	for line in sys.stdin:
		l=line.strip().split()
		if int(l[0])==1:
			lineCount=lineCount+1
			print "%dP\t%s\t%s" %(lineCount, l[1], l[2])
		else:
			print "%dC\t%s\t%s" %(fixedCounter+variableCounter, l[1], l[2])
			variableCounter=variableCounter+totalProfessorCount
	fixedCounter=fixedCounter+1
	variableCounter=0
	#Fill in your map code here. To write to output file, use "print" 
