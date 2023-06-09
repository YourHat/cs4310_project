from random import random, randint, seed
from math import pi, cos, sin
from cmath import log


class Point:
    x: float
    y: float

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return (
            self is not None
            and other is not None
            and abs(self.x - other.x) < 0.11
            and abs(self.y - other.y) < 0.11
        )

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


class LineSegment:
    a: Point
    b: Point

    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f'({self.a}, {self.b})'


def is_line_segment(a: Point, b: Point, c: Point) -> bool:
    '''
    is_line_segment is a function that returns True if point is a segment'''
    p0 = b.x - a.x, b.y - a.y
    p1 = c.x - a.x, c.y - a.y

    det = p0[0] * p1[1] - p1[0] * p0[1]
    prod = p0[0] * p1[0] + p0[1] * p1[1]

    return (
        (det == 0 and prod < 0)
        or (p0[0] == 0 and p0[1] == 0)
        or (p1[0] == 0 and p1[1] == 0)
    )


'''
is_in_polygon is a function that returns True if vertices is a polygon set
'''


def is_point_in_polygon(p: Point, Vertices: list[LineSegment]) -> bool:
    res = complex(0, 0)
    for i in range(1, len(Vertices) + 1):
        v0, v1 = Vertices[i - 1], Vertices[i % len(Vertices)]
        if is_line_segment(p, v0.a, v1.a):
            return False
        res += log(
            (complex(v1.a.x, v1.a.y) - complex(p.x, p.y))
            / (complex(v0.a.x, v0.a.y) - complex(p.x, p.y))
        )

    return abs(res) > 1


class Polygon:
    '''
    first : starting Point(x,y)
    segs : list of line segments making up polygon from first
    '''

    first: Point
    segs: list[LineSegment]

    def __init__(self) -> None:
        self.first = None
        self.segs = []

    '''
    function appends a point to a line segment
    '''

    def append(self, p: Point):
        if len(self.segs) == 0 and self.first == None:
            self.first = p
        elif self.first:
            self.segs.append(LineSegment(self.first, p))
            self.first = None
        else:
            last = self.segs.pop()
            new = LineSegment(last.b, p)
            self.segs.append(last)
            self.segs.append(new)

    def is_left_half(self, p: Point):
        '''
        function checks if point lies on the left half of the polygon
        '''
        return p.x < (max(self.segs, key=lambda p: p.a.x).a.x / 2)

    def is_top_half(self, p: Point):
        '''
        function checks if point is on the top half of the polygon
        '''
        return p.y > (max(self.segs, key=lambda p: p.a.y).a.y / 2)

    def add_indent(self):
        '''
        function creates an indentation of theta > 180 to the polygon
        '''
        size = len(self.segs)
        if size > 2:
            line_idx = randint(0, size - 1)
            line = self.segs[line_idx]

            min_x = min(line.a.x, line.b.x)
            min_y = min(line.a.y, line.b.y)
            new_p = Point(min_x, min_y)

            # TODO: this loops forever sometimes...
            while True:
                print(line.a == new_p or line.b == new_p)
                # TODO:
                # I'm sure there is a better way to do this...
                if not is_point_in_polygon(new_p, self.segs) or (
                    line.a == new_p or line.b == new_p
                ):
                    left, top = self.is_left_half(new_p), self.is_top_half(new_p)
                    right, bottom = not left, not top

                    if left and top:
                        new_p.x += 0.1
                        new_p.y -= 0.1
                    elif left and bottom:
                        new_p.x += 0.1
                        new_p.y += 0.1
                    elif right and top:
                        new_p.x -= 0.1
                        new_p.y -= 0.1
                    elif right and bottom:
                        new_p.x -= 0.1
                        new_p.y += 0.1

                    continue

                self.segs[line_idx].b = new_p
                self.segs.insert(line_idx + 1, LineSegment(new_p, line.b))
                print(line_idx)
                return
        else:
            raise Exception('less than 3 line segments')

    def __str__(self) -> str:
        return '\n'.join(str(seg) for seg in self.segs)


def generate_polygon(num_points, convex=True) -> Polygon:
    """
    To generate a simple (convex) polygon leave the second and third
    arguments `convex` and `cuts` alone.
    To generate a complex polygon (with no holes) `convex=False`.
    """
    points = [random() * (2.0 * pi) for _ in range(num_points + 1)]
    points.sort()

    poly = Polygon()
    x_o = 5.0
    y_o = 5.0
    r = 5.0
    for i, p in enumerate(points):
        # vacillate between `r` between 1 to 5 and `r` between 1 and last `r`
        if not convex:
            r = r + random() * (5 - r) if i % 2 else 1 + random() * (r - 1)
        poly.append(
            Point(
                x_o + r * cos(p),
                y_o + r * sin(p),
            )
        )

    return poly

