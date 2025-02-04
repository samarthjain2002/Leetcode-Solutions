"""
Accepted
2368 [Easy]
Runtime: 108 ms, faster than 95.28% of Python3 online submissions for Reachable Nodes With Restrictions.
Memory Usage: 63.30 MB, less than 97.13% of Python3 online submissions for Reachable Nodes With Restrictions.
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
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)

        uf = UnionFind(n)

        for edge in edges:
            a, b = edge
            if a in restricted or b in restricted:
                continue
            uf.union(a, b)

        root = uf.find(0)
        return uf.size[root]