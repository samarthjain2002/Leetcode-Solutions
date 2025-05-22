"""
Accepted
1334 [Medium]
Runtime: 227 ms, faster than 63.22% of Python3 online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
Memory Usage: 19.04 MB, less than 67.72% of Python3 online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
"""
# Dijkstra + minHeap approach
# TC: O(v * (v + e)log(v)), SC: O(v + e)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjMap = defaultdict(list)
        for fro, to, weight in edges:
            adjMap[fro].append((to, weight))
            adjMap[to].append((fro, weight))

        # Dijkstra from every node
        citiesReached = []
        for source in range(n):
            minHeap = [(0, source)]
            visited = set()
            reached = -1        # To offset for source node
            while minHeap:
                curDist, city = heapq.heappop(minHeap)
                if curDist > distanceThreshold:
                    break
                
                if city in visited:
                    continue
                visited.add(city)
                reached += 1

                for nei, dist in adjMap[city]:
                    if nei not in visited:
                        heapq.heappush(minHeap, (curDist + dist, nei))

            citiesReached.append(reached)
            

        # Find the city with smallest number of neighbors at threshold distance
        res, curMin = 0, float("inf")
        for city in range(n):
            if citiesReached[city] <= curMin:
                curMin = citiesReached[city]
                res = city
        return res



"""
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