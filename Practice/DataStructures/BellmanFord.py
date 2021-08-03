class Node:
    def __init__(self, s, e, w) -> None:
        self.start = s
        self.end = e
        self.weight = w

class Graph:
    def __init__(self, vertexCount) -> None:
        self.V = vertexCount
        self.graph = []

    def addEdge(self, s, e, weight):
        pass