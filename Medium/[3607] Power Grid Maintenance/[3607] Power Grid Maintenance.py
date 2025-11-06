"""
Accepted
3607 [Medium]
Runtime: 375 ms, faster than 57.11% of Python3 online submissions for Power Grid Maintenance.
Memory Usage: 101.62 MB, less than 94.85% of Python3 online submissions for Power Grid Maintenance.
"""
# Union-Find solution
# TC: O(q*c), SC: O(c)
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
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
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)

        for a, b in connections:
            uf.union(a, b)

        comps = defaultdict(list)
        for station in range(1, c + 1):
            root = uf.find(station)
            comps[root].append(station)

        for root, comp in comps.items():
            comps[root] = sorted(comp, reverse=True)

        offline = set()
        res = []
        for typ, x in queries:
            if typ == 2:
                offline.add(x)
                continue

            if x not in offline:
                res.append(x)
                continue
            
            root = uf.find(x)
            while comps[root] and comps[root][-1] in offline:
                comps[root].pop()

            if comps[root]:
                res.append(comps[root][-1])
            else:
                res.append(-1)

        return res