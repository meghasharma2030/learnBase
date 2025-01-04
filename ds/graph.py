from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, edge):
        if(node not in self.graph): self.graph[node] = []
        self.graph[node].append(edge)

    def bfs(self, start_node):
        visited = []
        queue = deque()
        queue.append(start_node)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                for node in self.graph[vertex]:
                    queue.append(node)
        return visited

    def dfs(self, start_node):
        visited = []
        stack = [start_node]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for node in self.graph[vertex]:
                    stack.append(node)
        return visited



def createGraph():
    graph = Graph()
    graph.addEdge("A", "B")
    graph.addEdge("A", "C")
    graph.addEdge("B", "A")
    graph.addEdge("B", "D")
    graph.addEdge("B", "E")
    graph.addEdge("C", "A")
    graph.addEdge("C", "F")
    graph.addEdge("D", "B")
    graph.addEdge("E", "B")
    graph.addEdge("E", "F")
    graph.addEdge("F", "C")
    graph.addEdge("F", "E")
    return graph

def tryItOut():
    graph = createGraph()
    print("graph",graph.graph)
    print("bfs:", graph.bfs("A"))
    print("dfs:", graph.dfs("A"))

tryItOut()