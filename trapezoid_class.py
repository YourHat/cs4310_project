
'''
Trapezoid Data Structure : http://www.polygontriangulation.com/2018/07/triangulation-algorithm.html
'''
class Trapezoid:
    def __init__(self) -> None:
        self.upper_vertex = high    # Upper vertex of the trapezoid
        self.lower_vertex = low     # Lower vertex of the trapezoid
        self.upper_adjacent = [0,0] # Up to two adjacent trapezoids above
        self.lower_adjacent = [0,0] # Up to two adjacent trapezoids below
        self.upper_third = (0,0)    # third extra region, whether region is left = 0 or right = 1
        self.left_segment = []      
        self.right_segment = []     # Left and right edges of the trapezoid
        self.sink = None            # Position of trapezoid in tree structure
        self.state = bool           # Represents validity of trapezoid, Inside = True or Outside = False

'''
Query Structure, binary tree.
'''
class QueryTree:
    def __init__(self) -> None:
        self.node_type = 'vertex/edge/trapezoid'
        self.segment_no = None      # Points to vertex or edge if node type is either vertex or edge
        self.trapezoid_no = None    # Points to trapezoid in trapezoid data structure if node type is trapezoid.
        self.left_child = left      # Points to left child node
        self.right_child = right    # Points to right child node
        self.parent_node = parent   # Points to parent node
