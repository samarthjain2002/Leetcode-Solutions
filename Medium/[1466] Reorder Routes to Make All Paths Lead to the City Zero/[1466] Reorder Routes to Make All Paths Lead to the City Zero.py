"""
Accepted
1466 [Medium]
Runtime: 195 ms, faster than 55.06% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
Memory Usage:  52.05 MB, less than 36.79% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = defaultdict(list)
        edges = set()
        for conn in connections:
            a, b = conn
            adjList[a].append(b)
            adjList[b].append(a)
            edges.add((a, b))

        self.res = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited and (nei, node) not in edges:
                    self.res += 1
                dfs(nei)

        dfs(0)
        return self.res