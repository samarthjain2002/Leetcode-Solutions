"""
Accepted
785 [Medium]
Runtime: 1 ms, faster than 57.45% of Python3 online submissions for Is Graph Bipartite.
Memory Usage: 18.25 MB, less than 86.20% of Python3 online submissions for Is Graph Bipartite.
"""
# BFS approach
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Everything uncolored initially
        color = [-1] * len(graph)
        
        for start in range(len(graph)):
            # Only first node of every component
            if color[start] == -1:
                color[start] = 0
                queue = deque([start])

                # Coloring the whole component
                while queue:
                    for i in range(len(queue)):
                        node = queue.popleft()
                        for nei in graph[node]:
                            if color[nei] == -1:
                                color[nei] = 1 - color[node]
                                queue.append(nei)
                            elif color[nei] == color[node]:
                                return False

        return True



"""
Runtime: 3 ms, faster than 44.98% of Python3 online submissions for Is Graph Bipartite.
Memory Usage: 18.79 MB, less than 15.39% of Python3 online submissions for Is Graph Bipartite.
"""
# DFS approach
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def dfs(node, col):
            color[node] = col

            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - col):
                        return False
                elif color[node] == color[nei]:
                    return False

            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
                    
        return True



"""
Runtime: 51 ms, faster than 7.39% of Python3 online submissions for Is Graph Bipartite.
Memory Usage: 18.93 MB, less than 5.46% of Python3 online submissions for Is Graph Bipartite.
"""
# Union-Find + DFS approach
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # To find each component
        uf = UnionFind(len(graph))
        for i, node in enumerate(graph):
            for nei in node:
                uf.union(i, nei)

        # Add the root node of each component to A
        A, B = set(), set()
        for node in range(len(graph)):
            A.add(uf.find(node))

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in graph[node]:
                if node in A:
                    B.add(nei)
                elif node in B:
                    A.add(nei)
                    
                dfs(nei)

        # Separate all the neighbors
        for node in A.copy():
            dfs(node)

        # If the neighbor is in the same set, it is not bipartite
        for i, node in enumerate(graph):
            for nei in node:
                if i in A and nei in A:
                    return False
                elif i in B and nei in B:
                    return False
        return True