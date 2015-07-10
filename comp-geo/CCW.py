
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C):
	# if slope of AC is bigger that slope of AB kinda stuff
	# considering the signs for (B.x - A.x) and (C.x - A.x) in a smart way 
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


a = Point(0,0)
b = Point(0,1)
c = Point(1,0)
d = Point(2,0)


print intersect(a,b,c,d)
# print intersect(a,c,b,d)
# print intersect(a,d,b,c)