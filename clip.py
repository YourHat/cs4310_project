class Point:
    x: int
    y: int


class LineSegment:
    x: Point
    y: Point


class Triangle:
    a: Point
    b: Point
    c: Point


def next_point(origin, triangles) -> Point:
    """
    Given a polygon and a point returns the next point clockwise.
    """
    pass


def neighbors(origin, seg) -> bool:
    """
    Given two line segments returns true if two points are connected.
    """
    pass


def left_most_segment(polygon) -> LineSegment:
    """
    Given a polygon returns the left most line segment clockwise.
    """
    pass


def make_triangle_from_line(origin, seg, triangles) -> Triangle:
    """
    Given a polygon returns the left most point.
    """
    if len(triangles) == 1:
        t = triangles[0]
        t.a = origin
        t.c = seg
    else:
        t = triangles.pop()
        t_new = Triangle(t.a, seg, t.c)
        triangles.append(t)
        triangles.append(t_new)


def ear_clip_mono_polygon(polygon):
    """
    Given a polygon returns the left most point.
    """
    # this is not important which point is picked
    origin = left_most_segment(polygon)
    triangles = [Triangle(a=None, b=next_point(origin, polygon), c=None)]
    for seg in polygon:
        if not neighbors(seg, origin):
            tri = make_triangle_from_line(origin, seg, triangles)
            triangles.append(tri)
        else:
            continue
