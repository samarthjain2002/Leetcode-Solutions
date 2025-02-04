"""
Accepted
2685 [Easy]
Runtime: 82 ms, faster than 26.88% of Python3 online submissions for Count the Number of Complete Components.
Memory Usage: 18.21 MB, less than 66.51% of Python3 online submissions for Count the Number of Complete Components.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
            elif self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
                self.size[root1] += self.size[root2]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        edges_from_node = [0] * n
        for edge in edges:
            a, b = edge
            edges_from_node[a] += 1
            edges_from_node[b] += 1
            uf.union(a, b)

        components = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            components[root].append(i)

        res = 0
        for root, nodes in components.items():
            if all(uf.size[root] == edges_from_node[node] + 1 for node in nodes):
                res += 1
        return res