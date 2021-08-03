"""
Reference : https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/#introDFSnBFS
and https://www.geeksforgeeks.org/graph-and-its-representations/

"""

class AdjNode:
    def __init__(self, data) -> None:
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest) -> None:
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self) -> None:
        for i in range(self.V):
            print(f"Adjacency list of vertex {i}\n head", end="")
            temp = self.graph[i]
            while temp:
                print(f" ->{temp.vertex}", end="")
                temp = temp.next

            print(" \n")

    def BreadthFirstSeach(self, s):
        visited = [False] * self.V

        queue = list()
        visited[s] = True
        queue.append(s)

        while (len(queue) != 0):
            s = queue[0]
            print(f"{s} ", end="")

            queue.pop(0)

            for i in range(len(self.graph)):
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
        


        

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    
    graph.add_edge(0,1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
    graph.BreadthFirstSeach(2)
