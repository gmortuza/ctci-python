import random
from Queue import Queue


class Node:

    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def add_adjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            raise Exception("No more adjacent node can't be added")

    def get_adjacent(self):
        return self.adjacent

    def get_vertex(self):
        return self.vertex

    def __str__(self):
        return str(self.vertex)


class Graph:
    def __init__(self):
        self.max_vertices = 6
        self.vertices = [0] * self.max_vertices
        self.count = 0

    def add_node(self, a_node):
        if self.count < self.max_vertices:
            self.vertices[self.count] = a_node
            self.count += 1
        else:
            raise Exception("Graph full")

    def get_nodes(self):
        return self.vertices


def create_new_graph():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 3)
    temp[1] = Node("b", 0)
    temp[2] = Node("c", 0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].add_adjacent(temp[1])
    temp[0].add_adjacent(temp[2])
    temp[0].add_adjacent(temp[3])
    temp[3].add_adjacent(temp[4])
    temp[4].add_adjacent(temp[5])

    for i in range(sizegraph):
        g.add_node(temp[i])
    return g

def create_new_graph_with_loop():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 1)
    temp[1] = Node("b", 1)
    temp[2] = Node("c", 1)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 2)
    temp[5] = Node("f", 0)

    temp[0].add_adjacent(temp[1])
    temp[1].add_adjacent(temp[2])
    temp[2].add_adjacent(temp[3])
    temp[3].add_adjacent(temp[4])
    temp[4].add_adjacent(temp[1])
    temp[4].add_adjacent(temp[5])

    for i in range(sizegraph):
        g.add_node(temp[i])
    return g


def is_root_exists(g, start, end):
    if start == end:
        return True

    queue1 = Queue()
    queue2 = Queue()
    queue1.put(start)
    queue2.put(end)
    visited = set([start, end])
    while not queue1.empty() and not queue2.empty():
        curr1 = queue1.get()
        curr2 = queue2.get()
        for vertex in curr1.get_adjacent():
            if vertex in visited:
                return True
            queue1.put(vertex)
            visited.add(vertex)
        for vertex in curr2.get_adjacent():
            if vertex in visited:
                return True
            queue2.put(vertex)
            visited.add(vertex)
    return False




g = create_new_graph()
n = g.get_nodes()
start = n[0]
end = n[5]
print "Start at:", start.get_vertex(), "End at: ", end.get_vertex()
print is_root_exists(g, start, end)