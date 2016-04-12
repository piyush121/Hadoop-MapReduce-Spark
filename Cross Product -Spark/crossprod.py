from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    
    #Create SparkContext 
    sc = SparkContext(appName="PythonCrossProduct")
    
    #Read first file: course data
    courses = sc.textFile(sys.argv[1], 1)

    #Read second file: professor data
    professors = sc.textFile(sys.argv[2], 1)

    #Write the code below to create an RDD that stores the cross product of the two tables and write the output
    myRdd=professors.cartesian(courses)
    output=myRdd.collect()
    for (courses, professors) in output:
        print("%s: %s" % (professors.encode('utf-8'), courses.encode('utf-8')))

    #Stop Spark
    sc.stop()
