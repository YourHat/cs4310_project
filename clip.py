import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class LineSegment:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

def next_point(origin, linesegment) -> Point:
    """
    Given a polygon and a point returns the next point clockwise.
    """
    if origin.a == linesegment.a or origin.b == linesegment.a:
        return linesegment.b
    else:
        return linesegment.a
        
def neighbors(origin, seg) -> bool:
    """
    Given two line segments returns true if two points are connected.
    """
    if set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((origin.a.x, origin.a.y),(origin.b.x, origin.b.y))): 
        return True
    else:
        return False

#def is_there_a_point(seg1, seg2, polygon) -> bool:
    #orgin_point = set(seg.a, seg.b) & set(next_seg.a, next_seg.b):
    #head_point = seg.point that is not originpoint
    #tail_point = next_seg.point that is not original point


        

def left_two_most_seg(polygon) -> tuple:
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
    Given a polygon returns the left most line segment clockwise.
    """
    origin_point = set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((seg_next.a.x, seg_next.a.y),(seg_next.b.x, seg_next.b.y))) 
    origin_point = Point(list(origin_point)[0][0],list(origin_point)[0][1])
    print(seg.a.x,seg.a.y, seg.b.x ,seg.b.y, seg_next.a.x,seg_next.a.y, seg_next.b.x ,seg_next.b.y)

    if seg.a.x == origin_point.x and seg.a.y == origin_point.y:
        head_point = seg.b
    else:
        head_point = seg.a
    if seg_next.a.x == origin_point.x and seg_next.a.y == origin_point.y:
        tail_point = seg_next.b
    else:
        tail_point = seg_next.a
    
    print("conv")
    print(head_point.x,origin_point.x, tail_point.y ,origin_point.y, head_point.x,origin_point.x, tail_point.y ,origin_point.y)
    if (((head_point.x - origin_point.x) * (tail_point.y - origin_point.y)) -  ((head_point.y - origin_point.y) * (tail_point.x - origin_point.x))) > 0:
        return True
    else:
        return False

def make_triangle(seg, seg_next, triangles) -> LineSegment:
    """
    Given a polygon returns the left most point.
    """
    origin_point = set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((seg_next.a.x, seg_next.a.y),(seg_next.b.x, seg_next.b.y))) 
    origin_point = Point(list(origin_point)[0][0],list(origin_point)[0][1])
    #print(origin_point)
    if seg.a.x == origin_point.x and seg.a.y == origin_point.y:
        head_point = seg.b
    else:
        head_point = seg.a
    if seg_next.a.x == origin_point.x and seg_next.a.y == origin_point.y:
        tail_point = seg_next.b
    else:
        tail_point = seg_next.a
    #if len(triangles) == 0:
    #    triangles[0] = Triangle(head_point, origin_point, tail_point)
        
    #else:
    triangles.append(Triangle(head_point, origin_point, tail_point))
    print(head_point.x, head_point.y ,tail_point.x, tail_point.y)
    time.sleep(2)
    return LineSegment(head_point, tail_point)

def ear_clip_mono_polygon(polygon):
    """
    Given a polygon returns the left most point.
    """
    global triangles 
    triangles = []

    for i in polygon:
        print(i)
    seg_next, seg_current = left_two_most_seg(polygon)
    polygon.remove(seg_next)
    polygon.remove(seg_current)
    seg_next = make_triangle(seg_current, seg_next, triangles)
    
    polygon.append(seg_next)
   
    
    seg_temp = None 
    print(seg_next.a.x, seg_next.b.x)
    while(len(polygon) > 3):
        for seg in polygon:
            print("for seg in polygon")
            print(seg.a.x, seg.a.y, seg.b.x, seg.b.y)
            if neighbors(seg, seg_next):
                print("they are neighbors")
                print((seg.a.x, seg.a.y),(seg.b.x, seg.b.y),  (seg_current.a.x, seg_current.a.y),(seg_current.b.x, seg_current.b.y) , (seg_next.a.x, seg_next.a.y),(seg_next.b.x, seg_next.b.y) )
                if not (set(((seg.a.x, seg.a.y),(seg.b.x, seg.b.y))) & set(((seg_current.a.x, seg_current.a.y),(seg_current.b.x, seg_current.b.y)))): 
                    print("not prev")
                    if is_convex(seg_next, seg):
                        print("convex")
                        print(seg_next)
                        print(seg)
                        print("in polygon")
                        for i in polygon:
                            print(i)
                        if seg in polygon: 
                            polygon.remove(seg)
                        if seg_next in polygon:
                            polygon.remove(seg_next)
                        seg_current = seg_next
                        seg_next = make_triangle(seg_current, seg, triangles)
                        polygon.append(seg_next)
                        break
            seg_temp = seg
                    
        else:
            seg_current = seg_next
            seg_next = seg_temp
        print("polygon")
        print(len(polygon))
        print("triangles")
        print(len(triangles))
        time.sleep(2)
    make_triangle(polygon[0],polygon[1], triangles)
    return triangles


def main():
    l1 = LineSegment(Point(0,3),Point(1,5))
    l2 = LineSegment(Point(1,5),Point(4,4))
    l3 = LineSegment(Point(4,4),Point(6,1))
    l4 = LineSegment(Point(6,1),Point(3,0))
    l5 = LineSegment(Point(3,0),Point(2,2))
    l6 = LineSegment(Point(2,2),Point(0,3))
    polygon1 = [l1,l2,l3,l4,l5,l6]
    print(ear_clip_mono_polygon(polygon1))
    l7 = LineSegment(Point(0,1),Point(2,2))
    l8 = LineSegment(Point(2,2),Point(1,4))
    l9 = LineSegment(Point(1,4),Point(4,3))
    l10 = LineSegment(Point(4,3),Point(3,1))
    l11 = LineSegment(Point(3,1),Point(4,0))
    l12 = LineSegment(Point(4,0),Point(0,1))
    polygon2 = [l7,l8,l9,l10,l11,l12]
    print(ear_clip_mono_polygon(polygon2))


main()
                     
