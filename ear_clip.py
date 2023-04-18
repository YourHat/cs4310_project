from gen_poly import generate_polygon, LineSegment, Point, Polygon


def neighbors(origin: LineSegment, next: LineSegment) -> bool:
    return origin.b == next.a or origin.a == next.b


def ear_clip(poly: Polygon) -> list[LineSegment]:
    lines = []
    origin = min(poly.segs, key=lambda seg: seg.a.x)
    for seg in poly.segs:
        if not neighbors(origin, seg):
            lines.append(LineSegment(origin.a, seg.a))
    return lines


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    poly = generate_polygon(8)

    # Make two lists
    coords = [(seg.a.x, seg.a.y) for seg in poly.segs]
    coords.append(coords[0])
    x, y = zip(*coords)

    plt.figure()
    plt.plot(x, y)
    # plt.show()

    i = 0
    for seg in ear_clip(poly):
        i += 1
        a_x, a_y = seg.a.x, seg.a.y
        b_x, b_y = seg.b.x, seg.b.y
        plt.plot([a_x, b_x], [a_y, b_y])

    plt.show()
