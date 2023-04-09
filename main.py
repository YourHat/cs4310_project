from random import randint

from gen_poly import generate_polygon
from clip import ear_clip_mono_polygon
from mono_decomp import polygon_decomposition

# To test ear clipping
for _ in range(100):
    convex = generate_polygon(randint(4, 100))
    traingulated = ear_clip_mono_polygon(convex)

    for tri in traingulated:
        assert tri.angle_total() == 180.00

# To test Seidel's polygon decomposition triangulation
for _ in range(100):
    num_points = randint(4, 100)
    convex = generate_polygon(
        num_points, convex=False, cuts=randint(1, num_points // 2)
    )
    traingulated = polygon_decomposition(convex)

    # TODO: could also pass a horizontal line making sure they are all
    # monotone
    for tri in traingulated:
        assert tri.angle_total() == 180.00
