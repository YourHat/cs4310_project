#ear clip


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self,a,b): #a,b are Point class
        self.a = a
        self.b = b

class Triangle: #a,b,c are Point class
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


def neighbors(origin, seg) -> bool:
    """
    Given two line segments returns true if two points are connected.
    """

    # if two lines have a same point, then return true
    if set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((origin.a.x, origin.a.y),(origin.b.x, origin.b.y))):
        return True
    else:
        return False

def is_there_a_point(seg, seg_next, polygon) -> bool:
    """
    Given two line segments returns true if there is no point in the triangle made by the two line segments
    two line with three points (origin_point - middle point, head_point, and tail_point)
    """
    # get all three points from the two given lines
    origin_point = set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((seg_next.a.x, seg_next.a.y),(seg_next.b.x, seg_next.b.y)))
    origin_point = Point(list(origin_point)[0][0],list(origin_point)[0][1])
    if seg.a.x == origin_point.x and seg.a.y == origin_point.y:
        head_point = seg.b
    else:
        head_point = seg.a
    if seg_next.a.x == origin_point.x and seg_next.a.y == origin_point.y:
        tail_point = seg_next.b
    else:
        tail_point = seg_next.a

    """
    calculate area of triangle with the two lines
    if the sum of triangles made with a point in polygon is the same, then return false
    """
    area_of_triangle = area_x2(origin_point.x, origin_point.y,head_point.x, head_point.y, tail_point.x, tail_point.y)
    for line in polygon:
        #skip if a point has the same coordinate as the three points for the triangle
        if (line.a.x, line.a.y) not in ((origin_point.x, origin_point.y),(head_point.x, head_point.y),(tail_point.x,tail_point.y)):
            if area_of_triangle == (area_x2(origin_point.x, origin_point.y,head_point.x, head_point.y, line.a.x, line.a.y) + area_x2(origin_point.x, origin_point.y,line.a.x, line.a.y, tail_point.x, tail_point.y) + area_x2(line.a.x, line.a.y,head_point.x, head_point.y, tail_point.x, tail_point.y)):
                return False
        #skip if a point has the same coordinate as the three points for the triangle
        if (line.b.x, line.b.y) not in ((origin_point.x, origin_point.y),(head_point.x, head_point.y),(tail_point.x,tail_point.y)):
            if area_of_triangle == (area_x2(origin_point.x, origin_point.y,head_point.x, head_point.y, line.b.x, line.b.y) + area_x2(origin_point.x, origin_point.y,line.b.x, line.b.y, tail_point.x, tail_point.y) + area_x2(line.b.x, line.b.y,head_point.x, head_point.y, tail_point.x, tail_point.y)):
                return False
    #if there is no point in the triangle, return true
    return True

def area_x2(x1,y1,x2,y2,x3,y3) -> int:
    """
    calculate an area of a triangle with three points
    can be negative, so returns absolute value
    returns twice the size of the triangles' area
    didnt want to cut in half, sicne you might get float value
    """
    return abs((x1 * (y2 -y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))


def left_two_most_seg(polygon) -> tuple:
    """
    returns two of the left most line segments for initialization
    left_up is the line segment that goes up from the left most point
    left_down is the line segment that goes down from the left most point
    it is to go though polygon clockwise
    """
    left_up = polygon[0]
    left_down = None
    for seg in polygon:
        if min(seg.a.x, seg.b.x) ==  min(left_up.a.x , left_up.b.x):
            left_down = seg
        elif min(seg.a.x, seg.b.x) < min(left_up.a.x , left_up.b.x):
            left_up = seg
    if min(left_up.a.y, left_up.b.y) < min(left_down.a.y , left_down.b.y):
        temp = left_up
        left_up = left_down
        left_down = temp

    return left_up, left_down


def is_convex(seg, seg_next) -> bool:
    """
    returns true if two line segments are convex (less than 180 degrees)
    """
    origin_point = set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((seg_next.a.x, seg_next.a.y),(seg_next.b.x, seg_next.b.y)))
    origin_point = Point(list(origin_point)[0][0],list(origin_point)[0][1])

    if seg.a.x == origin_point.x and seg.a.y == origin_point.y:
        head_point = seg.b
    else:
        head_point = seg.a
    if seg_next.a.x == origin_point.x and seg_next.a.y == origin_point.y:
        tail_point = seg_next.b
    else:
        tail_point = seg_next.a

    if (((head_point.x - origin_point.x) * (tail_point.y - origin_point.y)) -  ((head_point.y - origin_point.y) * (tail_point.x - origin_point.x))) > 0:
        return True
    else:
        return False

def make_triangle(seg, seg_next, triangles) -> LineSegment:
    """
    create a triangle with two given line segments, and returns line segment that is created to create the triangle
    """
    origin_point = set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((seg_next.a.x, seg_next.a.y),(seg_next.b.x, seg_next.b.y)))
    origin_point = Point(list(origin_point)[0][0],list(origin_point)[0][1])
    if seg.a.x == origin_point.x and seg.a.y == origin_point.y:
        head_point = seg.b
    else:
        head_point = seg.a
    if seg_next.a.x == origin_point.x and seg_next.a.y == origin_point.y:
        tail_point = seg_next.b
    else:
        tail_point = seg_next.a

    triangles.append(Triangle(head_point, origin_point, tail_point))
    return LineSegment(head_point, tail_point)

def ear_clip_mono_polygon(polygon) -> list[Triangle]:
    """
    Given a polygon returns a list of triangles made by triangulation - ear clipping
    """
    # declare triangles list as global variable, so that I can access to it from the make_triangle function
    global triangles
    triangles = []

    seg_next, seg_current = left_two_most_seg(polygon)

    found_tri = False #change it to True if there is a triangle you can create with a line segment
    seg_temp = None # used when there is no triangle you can create with a line segment
    while(len(polygon) > 3): #stop when there are three line segments left -> then create a triangle from the lines
        for seg in polygon:
            if neighbors(seg, seg_next):
                # if the neighbore line is counterclock wise, return false
                if not (set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((seg_current.a.x, seg_current.a.y),(seg_current.b.x, seg_current.b.y)))):
                    seg_temp = seg #used when there is no triangle you can create with a line segment
                    if is_convex(seg_next, seg):
                        if is_there_a_point(seg_next, seg, polygon):
                            # get rid of line segments used to create triangle from polygon list
                            if seg in polygon:
                                polygon.remove(seg)
                            if seg_next in polygon:
                                polygon.remove(seg_next)
                            seg_current = seg_next
                            seg_next = make_triangle(seg_current, seg, triangles)
                            polygon.append(seg_next) #add the line segments created to create triangle
                            found_tri = True
                    break
        # if there is no triangle you can create
        if not found_tri:
            seg_current = seg_next
            seg_next = seg_temp
        found_tri = False
    # when there are only three line segments left, create a triangle from the line segments
    make_triangle(polygon[0],polygon[1], triangles)
    return triangles


def ex1():
    #example 1
    l1 = LineSegment(Point(0,3),Point(1,5))
    l2 = LineSegment(Point(1,5),Point(4,4))
    l3 = LineSegment(Point(4,4),Point(6,1))
    l4 = LineSegment(Point(6,1),Point(3,0))
    l5 = LineSegment(Point(3,0),Point(2,2))
    l6 = LineSegment(Point(2,2),Point(0,3))
    polygon1 = [l1,l2,l3,l4,l5,l6]
    print("\noriginal lines in polygon")
    for line in polygon1:
        print(line.a.x,",",line.a.y, " - ",line.b.x,",", line.b.y)
    triangles = ear_clip_mono_polygon(polygon1)
    print("\ntrangles is")
    for triangle in triangles:
        print(triangle.a.x, ",", triangle.a.y," - ", triangle.b.x,",", triangle.b.y, " - ", triangle.c.x, ",",triangle.c.y,)

def ex2():
    #example 2
    l7 = LineSegment(Point(0,1),Point(2,2))
    l8 = LineSegment(Point(2,2),Point(1,4))
    l9 = LineSegment(Point(1,4),Point(4,3))
    l10 = LineSegment(Point(4,3),Point(3,1))
    l11 = LineSegment(Point(3,1),Point(4,0))
    l12 = LineSegment(Point(4,0),Point(0,1))
    polygon2 = [l7,l8,l9,l10,l11,l12]
    print("\noriginal line in polygon")
    for line in polygon2:
        print(line.a.x,",",line.a.y, " - ",line.b.x,",", line.b.y)
    triangles = ear_clip_mono_polygon(polygon2)
    print("\ntrangles is")
    for triangle in triangles:
        print(triangle.a.x, ",", triangle.a.y," - ", triangle.b.x,",", triangle.b.y, " - ", triangle.c.x, ",",triangle.c.y,)



#def temp_main():
#    ex1()
#    ex2()

#temp_main()

