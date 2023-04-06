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
    if set[origin.a, origin.b] & set[seg.a, seg.b]:
        return True
    else:
        return False

def is_there_a_point(seg1, seg2, polygon) -> bool:

    pass

def left_most_seg(polygon) -> LineSegment:
    left_seg = polygon[0]
    for seg in polygon:
        if min(seg.a.x, seg.b.x) < min(left_seg.a.x , left_seg.b.x):
            left_seg = seg
    retrun left_seg


def is_convex(seg, next_seg) -> bool:
    """
    Given a polygon returns the left most line segment clockwise.
    """
    

    return polygon[0]

def make_triangle_from_line(origin, seg, triangles) -> Triangle:
    """
    Given a polygon returns the left most point.
    """
    if len(triangles) == 1:
        triangles[0] = Triangle(origin.a, origin.b, seg.a or seg.b)
        
    else:
        #t = triangles.pop()
        t_new = Triangle(t.a, seg, t.c)
        triangles.append(t)
        triangles.append(t_new)


def ear_clip_mono_polygon(polygon):
    """
    Given a polygon returns the left most point.
    """
    # this is not important which point is picked
    origin = left_most_seg(polygon)

    triangles = [Triangle(None, None, None)]
    #remove origin and a segment in the first triangle from polygon

    for seg in polygon:
        if neighbors(seg, neighbore_seg):
            if (they can make triangle within the polygon):
                triangles.append[Triangle(a=neighbore_seg.a, b=next_point(neighbore_seg,seg), c=neighbore_seg.b)]



    
    #for seg in polygon:
    #    if not neighbors(seg, origin):
    #        tri = make_triangle_from_line(origin, seg, triangles)
    #        #triangles.append(tri)
    #    else:
    #        continue
