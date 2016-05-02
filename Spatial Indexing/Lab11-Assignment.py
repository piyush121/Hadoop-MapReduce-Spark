import csv
import StringIO
from rtree import index
import time
import sys

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Polygon:
	def __init__(self,points):
		self.points = points
		self.nvert = len(points)

		minx = maxx = points[0].x
		miny = maxy = points[0].y
		for i in xrange(1,self.nvert):
			minx = min(minx,points[i].x)
			miny = min(miny,points[i].y)
			maxx = max(maxx,points[i].x)
			maxy = max(maxy,points[i].y)

		self.bound = (minx,miny,maxx,maxy)


	def contains(self,pt):
		firstX = self.points[0].x
		firstY = self.points[0].y
		testx = pt.x
		testy = pt.y
		c = False
		j = 0
		i = 1
		nvert = self.nvert
		while (i < nvert) :
			vi = self.points[i]
			vj = self.points[j]
			
			if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
				c = not(c)

			if(vi.x == firstX and vi.y == firstY):
				i = i + 1
				if (i < nvert):
					vi = self.points[i];
					firstX = vi.x;
					firstY = vi.y;
			j = i
			i = i + 1
		return c

	def bounds(self):
		return self.bound


def taxiJFKTest():
	# Create a simple polygon
	start_time=time.time()
	poly = Polygon([Point(40.6188, -73.7712),Point(40.6233, -73.7674),Point(40.6248, -73.7681),Point(40.6281, -73.7657), Point(40.6356, -73.7472), Point(40.6422, -73.7468), Point(40.6469, -73.7534), Point(40.6460, -73.7544), Point(40.6589, -73.7745),Point(40.6628, -73.7858), Point(40.6634, -73.7891), Point(40.6655, -73.7903), Point(40.6658, -73.8021),Point(40.6632, -73.8146),Point(40.6638, -73.8210), Point(40.6621, -73.8244), Point(40.6546, -73.8248), Point(40.6469, -73.8212), Point(40.6302, -73.7848), Point(40.6223, -73.7899),Point(40.6203, -73.7831),Point( 40.6274, -73.7782),Point(40.6235, -73.7731),Point(40.6193, -73.7738),Point(40.6188, -73.7712)])
	count=0
	with open('taxigreen(06-15)_table.csv', 'rb') as csvfile:
		#cs=StringIO.StringIO(csvfile)
		spamreader = csv.reader(csvfile, delimiter=',')
		skip=0
		for row in spamreader:
			if(skip<2):
				skip=skip+1
				continue
			lat=float(row[2])
			lon=float(row[3])
			pt=Point(lat,lon)
			if poly.contains(pt):
				count=count+1
				#print "%f %f" %(lat,lon)
	end_time=time.time()-start_time
	print "Total number of drop-offs at JFK is %d" %(count)
	print "Total time taken = "+str(end_time)


def taxiLaGuardiaTest():
	
	start_time=time.time()
	# Create a simple polygon
	poly = Polygon([Point(40.7662, -73.8888),Point(40.7736, -73.8898),Point(40.7751, -73.8843),Point(40.7808, -73.8852), Point(40.7812, -73.8795), Point(40.7842, -73.8788), Point(40.7827, -73.8751), Point(40.7864, -73.8711),Point(40.788, -73.8673), Point(40.7832, -73.868), Point(40.7808, -73.8716), Point(40.773, -73.8534),Point(40.7697, -73.8557),Point(40.7673, -73.8505), Point(40.7645, -73.85), Point(40.7637, -73.8529), Point(40.7676, -73.856), Point(40.7659, -73.8594), Point(40.7654, -73.8625),Point(40.7693, -73.8672),Point(40.7714, -73.8732),Point(40.7697, -73.8871),Point(40.7665, -73.8866),Point(40.7662, -73.8888)])
	count=0
	
	with open('taxigreen(06-15)_table.csv', 'rb') as csvfile:
		#cs=StringIO.StringIO(csvfile)
		spamreader = csv.reader(csvfile, delimiter=',')
		skip=0
		for row in spamreader:
			if(skip<2):
				skip=skip+1
				continue
			lat=float(row[2])
			lon=float(row[3])
			pt=Point(lat,lon)
			if poly.contains(pt):
				count=count+1
				#print "%f %f" %(lat,lon)
	end_time=time.time()-start_time

	print "\nTotal number of drop-offs at Lagaurdia is %d" %(count)
	print "Total time taken = "+str(end_time)

def simpleRTree():
	print("\nR-tree test")

	idx = index.Index()
	with open('taxigreen(06-15)_table.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		skip=0
		i=0
		for row in spamreader:
			if(skip<2):
				skip=skip+1
				continue
			lat=float(row[2])
			lon=float(row[3])
			pt=Point(lat,lon)
			i=i+1
	# Insert the points into the R-tree index
			idx.insert(i,(pt.x,pt.y,pt.x,pt.y))
	start_time=time.time()

	# Query. This library only supports rectangular queries
	jfk = Polygon([Point(40.6188,-73.7712),Point(40.6233,-73.7674),Point(40.6248,-73.7681),Point(40.6281,-73.7657),Point(40.6356,-73.7472),Point(40.6422,-73.7468),Point(40.6469,-73.7534),Point(40.646,-73.7544),Point(40.6589,-73.7745),Point(40.6628,-73.7858),Point(40.6634,-73.7891),Point(40.6655,-73.7903),Point(40.6658,-73.8021),Point(40.6632,-73.8146),Point(40.6638,-73.821),Point(40.6621,-73.8244),Point(40.6546,-73.8248),Point(40.6469,-73.8212),Point(40.6302,-73.7848),Point(40.6223,-73.7899),Point(40.6203,-73.7831),Point(40.6274,-73.7782),Point(40.6235,-73.7731),Point(40.6193,-73.7738),Point(40.6188,-73.7712)])

	lga = Polygon([Point(40.7662,-73.8888),Point(40.7736,-73.8898),Point(40.7751,-73.8843),Point(40.7808,-73.8852),Point(40.7812,-73.8795),Point(40.7842,-73.8788),Point(40.7827,-73.8751),Point(40.7864,-73.8711),Point(40.788,-73.8673),Point(40.7832,-73.868),Point(40.7808,-73.8716),Point(40.773,-73.8534),Point(40.7697,-73.8557),Point(40.7673,-73.8505),Point(40.7645,-73.85),Point(40.7637,-73.8529),Point(40.7676,-73.856),Point(40.7659,-73.8594),Point(40.7654,-73.8625),Point(40.7693,-73.8672),Point(40.7714,-73.8732),Point(40.7697,-73.8871),Point(40.7665,-73.8866),Point(40.7662,-73.8888)])
	
	# Specify the bounds for JFK
	leftBottomX, leftBottomY, rightTopX, rightTopY = jfk.bounds()
	leftBottom = Point(float(leftBottomX),float(leftBottomY))
	rightTop = Point(float(rightTopX),float(rightTopY))

	# Perform the query
	results = list(idx.intersection((leftBottom.x,leftBottom.y,rightTop.x,rightTop.y), objects=True))
	cnt = 0
	for res in results:
		pt = Point(res.bbox[0],res.bbox[1])
		if (jfk.contains(pt)):
			cnt = cnt + 1
	end_time=time.time()-start_time
	print "\nJFK drop-offs "+str(cnt)
	print "Total time taken with spatial index = "+str(end_time)

	start_time=time.time()

	# Specify the bounds for LGA
	leftBottomX, leftBottomY, rightTopX, rightTopY = lga.bounds()
	leftBottom = Point(float(leftBottomX),float(leftBottomY))
	rightTop = Point(float(rightTopX),float(rightTopY))

	# Perform the query
	results = list(idx.intersection((leftBottom.x,leftBottom.y,rightTop.x,rightTop.y), objects=True))
	cnt =0
	for res in results:
		pt = Point(res.bbox[0],res.bbox[1])
		if lga.contains(pt):
			cnt = cnt + 1
	end_time=time.time()-start_time

	print "\nLagaurdia drop-offs "+str(cnt)
	print "Total time taken with spatial index = "+str(end_time)

print "Running on data without indexing..."
taxiJFKTest()
taxiLaGuardiaTest()
print "Running on data with spatial indexing now..."
simpleRTree()