"""
Accepted
3108 [Hard]
Runtime: 209 ms, faster than 41.30% of Python3 online submissions for Minimum Cost Walk in Weighted Graph.
Memory Usage: 93.57 MB, less than 36.96% of Python3 online submissions for Minimum Cost Walk in Weighted Graph.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return

        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.parent[par1] = par2
        else:            
            self.parent[par2] = par1
            self.rank[par1] += 1


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)

        # Constructing the graph
        for edge in edges:
            a, b, w = edge
            uf.union(a, b)

        # Every component will have the same minimum cost
        min_for_comp = {}
        # Mapping the root to the minimum cost
        for edge in edges:
            a, b, w = edge

            componentRoot = uf.find(a)
            if componentRoot not in min_for_comp:
                min_for_comp[componentRoot] = w
            # w1 & w1 will always be w1 anyway
            min_for_comp[componentRoot] &= w

        res = []
        for q in query:
            s, t = q
            # If there is no path (nodes of diff component)
            if uf.find(s) != uf.find(t):
                res.append(-1)
            else:
                res.append(min_for_comp[uf.find(s)])

        return res