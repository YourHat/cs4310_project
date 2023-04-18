from collections import deque
from random import seed

from gen_poly import generate_polygon


def area(p, q, r):
    '''Compute the signed area of the triangle defined by points p, q, and r.'''
    return (q[1] - p[1]) * (r[2] - p[2]) - (q[2] - p[2]) * (r[1] - p[1])


def seidel_triangulate(poly: list[tuple[float, float]]):
    '''Triangulate a simple polygon using Seidel's algorithm.
    poly: a list of (x, y) tuples representing the vertices of the polygon.
    Returns a list of triangular faces, where each face is a list of vertex indices.'''

    # Add indices to the vertices
    poly = [(i, x, y) for i, (x, y) in enumerate(poly)]

    # Sort vertices by x-coordinate, then by y-coordinate
    poly.sort(key=lambda p: (p[1], p[2]))
    print(poly)

    # Initialize a deque with the leftmost vertex and the two vertices immediately to its right
    que: deque[tuple[int, float, float]] = deque((poly[0], poly[1], poly[2]))

    # Initialize a list to hold the triangular faces
    faces: list[tuple[int, float, float]] = []

    # Iterate over the remaining vertices in order
    for i in range(3, len(poly)):
        p = poly[i]

        # If p is inside the current convex hull, remove all faces from the deque that are visible to p
        while len(que) > 1 and area(p, que[0], que[1]) > 0:
            faces.append((que[0][0], que[1][0], p[0]))
            que.popleft()

        # If p is outside the current convex hull, remove all faces from the deque and add the new edges formed by p
        if area(p, que[-1], que[0]) > 0:
            while len(que) > 1:
                faces.append((que[-1][0], que[0][0], p[0]))
                que.pop()
            que.append(p)
        else:
            que.append(p)

    # Add the remaining faces to the list
    while len(que) > 2:
        faces.append((que[0][0], que[1][0], que[2][0]))
        que.popleft()

    # Sort the faces by the index of their first vertex
    faces.sort()

    # Return the list of faces, without the vertex indices
    return [face[1:] for face in faces]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

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

        points = [(l.a.x, l.a.y) for l in poly.segs]
        for tri in chunks(seidel_triangulate(points), 2):
            print(tri)
            a_x, a_y = tri[0][0], tri[0][1]
            b_x, b_y = tri[1][0], tri[1][1]
            plt.plot([a_x, b_x], [a_y, b_y])

        plt.show()
        # plt.pause(3)
        # plt.clf()
