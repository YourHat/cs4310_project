from random import seed
import matplotlib.pyplot as plt
from time import time

from gen_poly import generate_polygon
from ear_clip import ear_clip
from mono_decomp import polygon_decomposition

from clip import clip


MAX_POINTS = 700
INC_BY = 100
START = 10
ROUNDS = 10

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
    for rounds in range(ROUNDS):
        seed(7)
        for nodes in range(START, MAX_POINTS, INC_BY):
            poly = generate_polygon(nodes)

            # Make two lists
            coords = [(seg.a.x, seg.a.y) for seg in poly.segs]
            coords.append(coords[0])
            x, y = zip(*coords)

            if rounds == 0 and SHOW_PLOT:
                plt.figure(nodes)
                plt.plot(x, y, color='black')

                for seg in timer(ear_clip, poly, time_map=EAR_MAP, iter=nodes):
                    a_x, a_y = seg.a.x, seg.a.y
                    b_x, b_y = seg.b.x, seg.b.y
                    plt.plot([a_x, b_x], [a_y, b_y])
                plt.show()
            else:
                _ = timer(ear_clip, poly, time_map=EAR_MAP, iter=nodes)

    final_time = {}
    for i, times in EAR_MAP.items():
        final_time.setdefault(i, sum(times) / ROUNDS)
    with open('ear_clip.csv', 'w') as f:
        f.write('number of nodes,time in ms\n')
        for nodes, t in final_time.items():
            f.write(f'{nodes},{t * 1000}\n')

    # To test ear clipping - for complex
    EAR_MAP = {}
    for rounds in range(ROUNDS):
        seed(7)
        for nodes in range(START, 600, INC_BY):
            poly = generate_polygon(nodes, convex=False)
            #poly = generate_polygon(nodes)
            # Make two lists
            coords = [(seg.a.x, seg.a.y) for seg in poly.segs]
            coords.append(coords[0])
            x, y = zip(*coords)

            if rounds == 0 and SHOW_PLOT:
                plt.figure(nodes)
                plt.plot(x, y, color='black')

                for seg in timer(clip, poly, time_map=EAR_MAP, iter=nodes):
                    a_x, a_y = seg.a.x, seg.a.y
                    b_x, b_y = seg.b.x, seg.b.y
                    plt.plot([a_x, b_x], [a_y, b_y])
                plt.show()
            else:
                _ = timer(clip, poly, time_map=EAR_MAP, iter=nodes)

    final_time = {}
    for i, times in EAR_MAP.items():
        final_time.setdefault(i, sum(times) / ROUNDS)
    with open('ear_clip_n.csv', 'w') as f:
        f.write('number of nodes,time in ms\n')
        for nodes, t in final_time.items():
            f.write(f'{nodes},{t * 999}\n')

    # To test monotone mountain polygon decomposition triangulation
    CONCAVE_MAP = {}
    for rounds in range(ROUNDS):
        seed(7)
        for nodes in range(START, MAX_POINTS, INC_BY):
            poly = generate_polygon(nodes, convex=False)

            # Make two lists
            coords = [(seg.a.x, seg.a.y) for seg in poly.segs]
            coords.append(coords[0])
            x, y = zip(*coords)

            if rounds == 0 and SHOW_PLOT:
                plt.figure(nodes)
                plt.plot(x, y, color='black')

                for seg in timer(polygon_decomposition, poly, time_map=CONCAVE_MAP, iter=nodes):
                    a_x, a_y = seg.a.x, seg.a.y
                    b_x, b_y = seg.b.x, seg.b.y
                    plt.plot([a_x, b_x], [a_y, b_y])
                plt.show()
            else:
                _ = timer(polygon_decomposition, poly, time_map=CONCAVE_MAP, iter=nodes)

    final_time = {}
    for i, times in CONCAVE_MAP.items():
        final_time.setdefault(i, sum(times) / ROUNDS)
    with open('poly_decomp.csv', 'w') as f:
        f.write('number of nodes,time in ms\n')
        for nodes, t in final_time.items():
            f.write(f'{nodes},{t * 1000}\n')

if __name__ == '__main__':
    main()
