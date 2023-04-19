from random import random, seed
import matplotlib.pyplot as plt


def det(ax, ay, bx, by, cx, cy):
    return (ax - bx) * (cy - by) - (cx - bx) * (ay - by)


def gen_concave_poly(n):
    assert n >= 3

    ax, ay = random(), random()
    bx, by = random(), random()
    cx, cy = random(), random()

    if not det(ax, ay, bx, by, cx, cy) < 0:
        ax, ay, cx, cy = cx, cy, ax, ay

    points = [(ax, ay), (bx, by), (cx, cy)]

    def do_lines_intersect(p1, p2, p3, p4):
        (x1, y1) = p1
        (x2, y2) = p2
        (x3, y3) = p3
        (x4, y4) = p4
        denominator = x1 * (y4 - y3) + x2 * (y3 - y4) + x4 * (y2 - y1) + x3 * (y1 - y2)

        s = +(x1 * (y4 - y3) + x3 * (y1 - y4) + x4 * (y3 - y1)) / denominator
        t = -(x1 * (y3 - y2) + x2 * (y1 - y3) + x3 * (y2 - y1)) / denominator
        return 0 < s < 1 and abs(s - 1) > 0.00001 and 0 < t < 1 and abs(t - 1) > 0.00001

    def crosses_polygon(a, b):
        for i in range(len(points)):
            if do_lines_intersect(a, b, points[i], points[(i + 1) % len(points)]):
                return True
        return False

    for _ in range(3, n):
        new = random(), random()
        for j in range(len(points)):
            if not crosses_polygon(points[j], new) and not crosses_polygon(
                new, points[(j + 1) % len(points)]
            ):
                points.insert(j + 1, new)
                break
        else:
            assert not "something went wrong (probably float math again)"

    return points


if __name__ == '__main__':
    # points = gen_concave_poly(5)
    # points = gen_concave_poly(15)
    # points = gen_concave_poly(50)
    # points = gen_concave_poly(100)

    points = gen_concave_poly(20)

    for i in range(len(points)):
        ax, ay = points[i]
        bx, by = points[(i + 1) % len(points)]
        plt.plot([ax, bx], [ay, by], color='black')

    plt.show()
    plt.clf()
