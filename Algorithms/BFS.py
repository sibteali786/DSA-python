
num_nodes = 8
edges = [(1,2), (1,4), (2,3), (2,5), (2,7), (3,1), (4,3), (5,8), (7,6), (8,7), (8,6)]

print(num_nodes, len(edges))

# where number of nodes start from 0 instead of 1 and end at 7 instead of 8
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            n1 = n1 - 1
            n2 = n2 - 1
            self.data[n1].append(n2)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n,neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


graph1 = Graph(num_nodes,edges)
print(graph1)

def dfs(graph,root):
    stack = []
    discovered = [False] * len(graph.data)
    stack.append(root)
    result = []
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] =  True
            result.append(current)
            for node in graph.data[current]:
                stack.append(node)
    return result

print(dfs(graph1,0))

def allPathDFS(graph,root,goal):
    newArray = []
    while(True):
        stack = []
        discovered = [False] * len(graph.data)
        stack.append(root)
        result = []
        while len(stack) > 0:
            current = stack.pop()
            if current is goal:
                result.append(current)
                break
            if not discovered[current]:
                discovered[current] = True
                if current not in newArray:
                    result.append(current)
                    for node in graph.data[current]:
                        stack.append(node)
        print(result)
        newArray = result



print(allPathDFS(graph1,0,7))

