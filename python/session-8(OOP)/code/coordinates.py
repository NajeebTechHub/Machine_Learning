# Write oop classes to handle the following scenarios
# a user can create and view 2D coordinates
# a user can find out the distance between two coordinates
# a user can find the distance of coordinate from origin
# a user can check if a point lies on given line
# a user can find the distance between a given 2D point and a given line


class Point:

    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cord,self.y_cord)
    
    def euclidean_distance(self,other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
    



class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {}'.format(self.A,self.B,self.C)
    
    def point_on_line(line,point):
        if line.A * point.x_cord + line.B * point.y_cord + line.C == 0:
            print('point lie on line')
        else:
            print("point doest't lie on the line ")


# p1 = Point(1,1)
# p2 = Point(1,1)
# print(p1.euclidean_distance(p2))

# print(p1.distance_from_origin())

# l1 = Line(2,5,7)
# print(l1)

p1 = Point(1,1)
l1 = Line(1,1,-2)
print(l1.point_on_line(p1))