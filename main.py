from random import seed
import matplotlib.pyplot as plt
from time import time

from gen_poly import generate_polygon, Polygon, Point
from gen_crazy_poly import gen_concave_poly
from ear_clip import ear_clip
from mono_decomp import polygon_decomposition

MAX_POINTS = 100
INC_BY = 10
START = 10
ROUNDS = 1

SHOW_PLOT = True

def timer(func, *args, time_map: dict[int, list[float]], iter: int):
    a = time()
    res = func(*args)
    b = time()
    time_map.setdefault(iter, []).append(b - a)
    return res

def main():
    # To test ear clipping
    EAR_MAP = {}
    seed(9)
    for nodes in range(START, MAX_POINTS, INC_BY):
        for rounds in range(ROUNDS):
            poly = generate_polygon(nodes)

            if rounds == 0 and SHOW_PLOT:
                # Make two lists
                coords = [(seg.a.x, seg.a.y) for seg in poly.segs]
                coords.append(coords[0])
                x, y = zip(*coords)

                plt.figure(nodes)
                plt.plot(x, y, color='black')

                for seg in timer(ear_clip, poly, time_map=EAR_MAP, iter=nodes):
                    a_x, a_y = seg.a.x, seg.a.y
                    b_x, b_y = seg.b.x, seg.b.y
                    plt.plot([a_x, b_x], [a_y, b_y])
                plt.show()
            else:
                _ = timer(ear_clip, poly, time_map=EAR_MAP, iter=nodes)

    # final_time = {}
    # for i, times in EAR_MAP.items():
    #     final_time.setdefault(i, sum(times) / ROUNDS)
    # with open('ear_clip.csv', 'w') as f:
    #     f.write('number of nodes,time in ms\n')
    #     for nodes, t in final_time.items():
    #         f.write(f'{nodes},{t * 1000}\n')

    # To test monotone mountain polygon decomposition triangulation
    CONCAVE_MAP = {}
    seed(9)
    for nodes in range(START, MAX_POINTS, INC_BY):
        for rounds in range(ROUNDS):
            # poly = generate_polygon(nodes, convex=False)
            poly = Polygon()
            points = gen_concave_poly(nodes)
            for p in points:
                poly.append(Point(p[0], p[1]))

            if rounds == 0 and SHOW_PLOT:
                 # Make two lists
                coords = [(seg.a.x, seg.a.y) for seg in poly.segs]
                coords.append(coords[0])
                x, y = zip(*coords)

                plt.figure(nodes)
                plt.plot(x, y, color='black')

                for seg in timer(polygon_decomposition, poly, time_map=CONCAVE_MAP, iter=nodes):
                    a_x, a_y = seg.a.x, seg.a.y
                    b_x, b_y = seg.b.x, seg.b.y
                    plt.plot([a_x, b_x], [a_y, b_y])
                plt.show()
            else:
                _ = timer(polygon_decomposition, poly, time_map=CONCAVE_MAP, iter=nodes)

    # final_time = {}
    # for i, times in CONCAVE_MAP.items():
    #     final_time.setdefault(i, sum(times) / ROUNDS)
    # with open('poly_decomp.csv', 'w') as f:
    #     f.write('number of nodes,time in ms\n')
    #     for nodes, t in final_time.items():
    #         f.write(f'{nodes},{t * 1000}\n')

if __name__ == '__main__':
    main()
