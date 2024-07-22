"""
Accepted
547 [Medium]
Runtime: 257 ms, faster than 5.04% of Python3 online submissions for Number of Provinces.
Memory Usage:  19.99 MB, less than 5.79% of Python3 online submissions for Number of Provinces.
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return None
            if node not in visited:
                visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)

        adjList = defaultdict(set)
        comb = set()
        for conn in isConnected:
            provs = []
            for i, prov in enumerate(conn):
                if prov:
                    provs.append(i)
            for c in combinations(provs, 2):
                comb.add(c)

        for a, b in comb:
            adjList[a].add(b)
            adjList[b].add(a)

        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)

        return count