from random import seed

from gen_poly import (
    Point,
    LineSegment,
    Polygon,
    generate_polygon,
)


def point_in_poly(x: float, y: float, poly: list[Point]):
    """
    Check if a point is inside a polygon.
    """
    n = len(poly)
    inside = False

    p1x, p1y = poly[0].x, poly[0].y
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n].x, poly[i % n].y
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def do_lines_intersect(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    x3: float,
    y3: float,
    x4: float,
    y4: float,
):
    """
    Given two line segments (x1,y1)-(x2,y2) and (x3,y3)-(x4,y4),
    returns True if the segments intersect, False otherwise.
    """
    # calculate the direction of each line segment
    dx1 = x2 - x1  # a
    dy1 = y2 - y1  # b
    dx2 = x4 - x3  # c
    dy2 = y4 - y3  # d

    # calculate the determinant of the matrix formed by the direction vectors
    det = dx1 * dy2 - dx2 * dy1 # f

    # if the determinant is zero, the lines are parallel and do not intersect
    if det == 0:
        return True

    # determine if
    # ua = (dx2 * (y1 - y3) - dy2 * (x1 - x3)) / det
    # ua = (dx2 * (y1 - y3) + dy2 * x3 - dy2 * x1) / det  # s
    # ua = (dx2 * (y1 - y2) + (dy2 * x2) - (dy2 * x1)) / det
    s = (x1 * (y4 - y3) + x3 * (y1 - y4) + x4 * (y3 - y1)) / (
        x1 * (y4 - y3) + x2 * (y3 - y4) + x4 * (y2 - y1) + x3 * (y1 - y2)
    )

    # ub = (dx1 * (y1 - y3) - dy1 * (x1 - x3)) / det
    # ub = (dx1 * (y1 - y3) + dy1 * x3 - dy1 * x1) / det  # t
    t = -(x1 * (y3 - y2) + x2 * (y1 - y3) + x3 * (y2 - y1)) / (
        x1 * (y4 - y3) + x2 * (y3 - y4) + x4 * (y2 - y1) + x3 * (y1 - y2)
    )
    # ub = (dx1 * (y1 - y2) + (dy1 * x2) - (dy1 * x1)) / det
    print(s, t)
    # if both parameters are between 0 and 1, the line segments intersect
    if 0.0 < s < 1.0 and 0.0 < t < 1.0:
        return True
    else:
        return False


def line_in_poly(x1: float, y1: float, x2: float, y2: float, poly: list[Point]):
    """
    Check if a line segment is entirely inside a polygon.
    """

    # if not point_in_poly(x1, y1, poly) or not point_in_poly(x2, y2, poly):
    #     print('endpoints not in polygon')
    #     return False

    for i in range(len(poly)):
        x3, y3 = poly[i].x, poly[i].y
        x4, y4 = poly[(i + 1) % len(poly)].x, poly[(i + 1) % len(poly)].y
        if do_lines_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
            print('lines intersect', (x1, y1), (x2, y2), (x3, y3), (x4, y4))
            return False

    return True


def is_line_in_polygon(seg: LineSegment, poly: list[Point]):
    return line_in_poly(seg.a.x, seg.a.y, seg.b.x, seg.b.y, poly)


def sub(a, b):
    return Point(a.x - b.x, a.y - b.y)


def det(a, b):
    return a.x * b.y - b.x * a.y


def in_triangle(a, b, c, x):
    return (
        True
        and det(sub(a, x), sub(b, x)) > 0
        and det(sub(b, x), sub(c, x)) > 0
        and det(sub(c, x), sub(a, x)) > 0
    )


def is_triangle_left(a: Point, b: Point, c: Point):
    """
    Determine if the `b` point is inside the polygon.
    """
    d1x = a.x - b.x
    d1y = a.y - b.y
    d2x = c.x - b.x
    d2y = c.y - b.y

    # Determinate tells us which side our new triangles b point
    # points (in to the polygon is positive, negative means it
    # is inside the polygon and points outwards)
    #
    # This is only fooled by a specific shape which is why for all
    # points they must be `in_triangle`
    det = d1x * d2y - d2x * d1y
    return det < 0.0


def polygon_decomposition(poly: Polygon) -> list[LineSegment]:
    """
    `polygon_decomposition` is an incremental randomized algorithm whose expected
    complexity is O(n log*n). In practice, it is almost linear time for a simple
    polygon having n vertices (simple meaning no holes).
    """

    # const_points = [s.a for s in poly.segs]
    lines = []
    points = [s for s in poly.segs]
    while len(points) > 3:
        a, b, c = (
            points[0],
            points[1],
            points[2],
        )
        if is_triangle_left(a.a, b.a, c.a) and all(
            not in_triangle(a.a, b.a, c.a, x.a) for x in points[3:]
        ):
            points.pop(1)
            lines.append(LineSegment(a.a, c.a))
            b, c = c, points[2]
            while (
                len(points) > 3
                and is_triangle_left(a.a, b.a, c.a)
                and all(not in_triangle(a.a, b.a, c.a, x.a) for x in points[3:])
            ):
                points.pop(1)
                lines.append(LineSegment(a.a, c.a))
                b, c = c, points[2]
        points.append(points.pop(0))

    return lines


def timer(func, *args):
    from time import time

    a = time()
    res = func(*args)
    b = time()
    print(b - a)
    return res


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    seed(int(input()))
    for stupid in range(10, 1000, 100):
        print('number of points', stupid)

        poly = generate_polygon(stupid, convex=False)

        print('poly len', len(poly.segs))

        # Make two lists
        coords = [(seg.a.x, seg.a.y) for seg in poly.segs]
        coords.append(coords[0])
        x, y = zip(*coords)

        print(len(x))
        plt.figure(stupid)
        plt.plot(x, y, color='black')

        i = 0
        for seg in timer(polygon_decomposition, poly):
            i += 1
            a_x, a_y = seg.a.x, seg.a.y
            b_x, b_y = seg.b.x, seg.b.y
            plt.plot([a_x, b_x], [a_y, b_y])

        plt.show()
        # plt.pause(3)
        # plt.clf()
