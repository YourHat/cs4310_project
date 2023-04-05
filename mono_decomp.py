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


class Trapezoid:
    a: Point
    b: Point
    c: Point
    d: Point


def add_horizontal_line_from_connecting_vertex(line_a, line_b, trapezoids):
    """
    `line_a` connects to `line_b` at `v`, there are 3 options for adding the
    horizontal line.
    """
    horizontal_line = LineSegment()
    if line_a.is_above(horizontal_line) and line_b.is_below(horizontal_line):
        remove_line(trapezoids, line_a)
        add_line(trapezoids, line_b)
    elif line_a.is_above(horizontal_line) and line_b.is_above(horizontal_line):
        remove_line(trapezoids, line_a, line_b)
    elif line_a.is_below(horizontal_line) and line_b.is_below(horizontal_line):
        add_line(trapezoids, line_a, line_b)


def horizontal(line_a, line_b) -> bool:
    pass


def last_seg(trapezoids) -> LineSegment:
    pass

def last_trap(trapezoids) -> Trapezoid:
    pass

def monotone_polygon(trapezoids):
    pass


def decompose_poly_to_trap(polygon) -> list[Trapezoid]:
    """
    `decompose_poly_to_trap` Uses a random ordering of segments it incrementally builds
    trapezoids from segments. It checks that 2 given segments are not horizontal since
    using parallel segments increases number of trapezoids. It "draws" additional horizontal
    lines from vertices to create monotone polygon's of the trapezoids (it draws a line
    that only connects with 2 segments).
    """

    trapezoids = []
    # sort all points by `y` coordinate
    sort(polygon, lambda point: point.y)
    prev_seg = polygon.remove(0)
    for seg in polygon:
        if not horizontal(prev_seg, seg):
            add_horizontal_line_from_connecting_vertex(prev_seg, seg, trapezoids)
        prev_seg = seg

    decompose_trap_to_mono(trapezoids)


def decompose_trap_to_mono(trapezoid):
    """
    `decompose_trap_to_mono` Removes trapezoids that fail the monotone polygon test.
    """
    if not monotone_polygon(trapezoid):
        # TODO: fix non mono trapezoid somehow, may need polygon list too or last few traps?
        pass


def cut_traps_in_half(mono_traps):
    """
    `cut_traps_in_half` Make a line from opposite corners.

    """
    for trap in mono_traps:
        # add a line from trap.a to trap.c or another diagonal points
        # checking if this is already just a triangle
        pass


def polygon_decomposition(polygon) -> list[Triangle]:
    """
    `polygon_decomposition` is an incremental randomized algorithm whose expected
    complexity is O(n log*n). In practice, it is almost linear time for a simple
    polygon having n vertices (simple meaning no holes).
    """
    trapezoids = decompose_poly_to_trap(polygon)
    mono = decompose_trap_to_mono(polygon, trapezoids)
    triangulated_polygon = cut_traps_in_half(mono)
