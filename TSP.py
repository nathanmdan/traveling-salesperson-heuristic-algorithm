# Nathan Dan
# CS325 W25
# Assignment 9
# 03-12-2025

def solve_tsp(G: list) -> list[int]:
    """
    Solves the Traveling Salesperson problem for a given graph using a nearest neighbor heuristic algorithm.
    Returns a list of vertex indices, starting and ending with the first vertex.
    """
    nodes = len(G)
    node = 0
    next_node = 0

    # Initialize a TSP path starting at node 0 and keep track of visited nodes with a set.
    tsp_path = [0]
    visited = {0}

    # Iterate through the neighboring nodes and travel to the next closest unvisited node.
    while len(visited) < nodes:
        min_edge = float('inf')
        for i in range(nodes):
            edge = G[node][i]
            if 0 < edge < min_edge and i not in visited:
                next_node = i
                min_edge = edge
        tsp_path.append(next_node)
        visited.add(next_node)
        node = next_node

    # After all other nodes are visited, return to node 0 to complete the path.
    tsp_path.append(0)

    return tsp_path

# input_graph = [
#     [0, 2, 3, 20, 1],
#     [2, 0, 15, 2, 20],
#     [3, 15, 0, 20, 13],
#     [20, 2, 20, 0, 9],
#     [1, 20, 13, 9, 0],
# ]
# print(solve_tsp(input_graph))
