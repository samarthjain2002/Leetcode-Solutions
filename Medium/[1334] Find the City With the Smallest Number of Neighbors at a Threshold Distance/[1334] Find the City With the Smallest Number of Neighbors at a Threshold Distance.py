"""
Accepted
1334 [Medium]
Runtime: 1371 ms, faster than 5.01% of Python3 online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
Memory Usage:  17.74 MB, less than 67.75% of Python3 online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjList = defaultdict(dict)
        for fro, to, weight in edges:
            adjList[fro][to] = weight
            adjList[to][fro] = weight

        def dfs(node, currentDistance):
            for neighbor, weight in adjList[node].items():
                newDistance = currentDistance + weight
                if newDistance <= distanceThreshold and newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance
                    dfs(neighbor, newDistance)

        minCount = float("inf")
        res = 0

        for source in range(n):
            distances = [float("inf") for _ in range(n)]
            distances[source] = 0
            dfs(source, 0)
            
            count = sum(1 for i, d in enumerate(distances) if i != source and d <= distanceThreshold)
            if count <= minCount:
                minCount = count
                res = source

        return res