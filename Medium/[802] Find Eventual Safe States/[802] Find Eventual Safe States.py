"""
Accepted
802 [Medium]
Runtime: 46 ms, faster than 55.92% of Python3 online submissions for Find Eventual Safe States.
Memory Usage: 23.70 MB, less than 39.31% of Python3 online submissions for Find Eventual Safe States.
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        safe = {}

        def isSafe(node):
            if node in safe:
                return safe[node]

            safe[node] = False
            for nei in graph[node]:
                if not isSafe(nei):
                    return False
            safe[node] = True
            return True

        res = []
        for i in range(N):
            if isSafe(i):
                res.append(i)
        return res