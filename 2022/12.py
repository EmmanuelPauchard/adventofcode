from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import numpy as np

test_data = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

with open("2022/12.in") as f:
    data = f.read()

step = 2

lines = test_data.strip().split("\n")
vertices = test_data.replace("\n", "")
# lines = data.strip().split("\n")
# vertices = data.replace("\n", "")

# Note start and target position but replace with real values
start_pos = vertices.index("S")
target = vertices.index("E")
vertices = vertices.replace("S", "a")
vertices = vertices.replace("E", "z")

WIDTH = len(lines[0])
HEIGHT = len(lines)

edges = np.zeros((len(vertices), len(vertices)), np.int8)


def is_allowed(s, e):
    """
    return True if transition from vertex s to vertex e is allowed
    :param s,e: vertex, as index in vertices
    """
    return ord(vertices[s]) + 1 >= ord(vertices[e])


def find_neighbors(vertex):
    """
    return the number of accessible neighbors of the given vertex
    :param vertex: vertex, as index in vertices
    :param list[vertex], accessible neighbors, as indices in vertices
    """
    neighbors = []
    # 4 possible directions
    if vertex % WIDTH < WIDTH - 1 and is_allowed(vertex, vertex + 1):
        # Right
        neighbors += [vertex + 1]
    if vertex % WIDTH > 0 and is_allowed(vertex, vertex - 1):
        # Left
        neighbors += [vertex - 1]
    if vertex // WIDTH > 0 and is_allowed(vertex, vertex - WIDTH):
        # Up
        neighbors += [vertex - WIDTH]
    if vertex // WIDTH < HEIGHT - 1 and is_allowed(vertex, vertex + WIDTH):
        # Down
        neighbors += [vertex + WIDTH]

    return neighbors


# Construct the matrix of edges: [i,j] = 1 <=> transition is possible from i to j
for i, v in enumerate(vertices):
    for neighbors in find_neighbors(i):
        edges[i][neighbors] = 1

# Converse the array to sparse matrix and use scipy shortest_path
# graph is directed because a->c is not allowed, whereas c->a is
# graph is unweighted, we only compute the number of steps
# predecessors is only used to draw the path
graph = csr_matrix(edges)
dist_matrix, predecessors = shortest_path(
    csgraph=graph,
    unweighted=True,
    directed=True,
    return_predecessors=True,
)

if step == 1:
    # shortest path from start to target
    print(
        f"Shortest path to {target} from {start_pos} ", dist_matrix[start_pos, target]
    )
    # display path
    p = predecessors[start_pos, target]
    while True:
        if p < 0:
            print("")
            break
        print(p, end=" <- ")
        p = predecessors[start_pos, p]
else:
    # filter all start positions where level is a, then get the min of distances
    start_indices_from_a = [i for i, v in enumerate(vertices) if v == "a"]
    print(
        f"Minimum distance: ",
        min([dist_matrix[a, target] for a in start_indices_from_a]),
    )
