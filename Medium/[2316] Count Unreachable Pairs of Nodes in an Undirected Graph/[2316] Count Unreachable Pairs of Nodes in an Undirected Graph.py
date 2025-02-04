"""
Accepted
2316 [Easy]
Runtime: 341 ms, faster than 6.19% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
Memory Usage: 64.94 MB, less than 90.46% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.rank[root1] += self.rank[root2]
                self.parent[root2] = root1
            else:
                self.rank[root2] += self.rank[root1]
                self.parent[root1] = root2


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            a, b = edge
            uf.union(a, b)

        component_size = defaultdict(int)
        for i in range(n):
            root = uf.find(i)
            component_size[root] += 1

        # Compute the total possible edges
        total_pairs = (n * (n - 1)) // 2

        # Subtract internal edges within each component
        internal_edges = sum((size * (size - 1)) // 2 for size in component_size.values())

        # The number of inter-component edges
        return total_pairs - internal_edges