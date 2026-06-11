"""
Accepted
3558 [Medium]
Runtime: 435 ms, faster than 30.11% of Python3 online submissions for Number of Ways to Assign Edge Weights I.
Memory Usage: 68.72 MB, less than 64.52% of Python3 online submissions for Number of Ways to Assign Edge Weights I.
"""
# BFS Solution
# TC: O(n), SC: O(n)
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Build tree
        edgeMap = defaultdict(list)
        for edge in edges:
            a, b = edge
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        # Find the maximum depth using BFS
        visited = set([1])
        queue = deque([1])
        n = -1
        while queue:
            n += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                for nei in edgeMap[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

        return pow(2, n - 1, MOD)



"""
Runtime: 372 ms, faster than 60.21% of Python3 online submissions for Number of Ways to Assign Edge Weights I.
Memory Usage: 127.27 MB, less than 12.90% of Python3 online submissions for Number of Ways to Assign Edge Weights I.
"""
# DFS Solution
# TC: O(n), SC: O(n)
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Build tree
        edgeMap = defaultdict(list)
        for edge in edges:
            a, b = edge
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        # Find the maximum depth using DFS
        def dfs(node, parent):
            depth = 0
            for nei in edgeMap[node]:
                # Since it is a tree, we need not worry about cycles
                if nei != parent:
                    depth = max(depth, dfs(nei, node) + 1)
            return depth

        n = dfs(1, 0)
        return pow(2, n - 1, MOD)



"""
Runtime: 480 ms, faster than 16.13% of Python3 online submissions for Number of Ways to Assign Edge Weights I.
Memory Usage: 138.97 MB, less than 6.45% of Python3 online submissions for Number of Ways to Assign Edge Weights I.
"""
# DFS Solution
# TC: O(n), SC: O(n)
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Build tree
        edgeMap = defaultdict(list)
        for edge in edges:
            a, b = edge
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        # Find the maximum depth using DFS
        visited = {1}
        def dfs(node):
            depth = 0
            for nei in edgeMap[node]:
                if nei not in visited:
                    visited.add(nei)
                    depth = max(depth, dfs(nei) + 1)
            return depth

        n = dfs(1)
        return pow(2, n - 1, MOD)