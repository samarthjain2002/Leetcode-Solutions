"""
Accepted
743 [Medium]
Runtime: 397 ms, faster than 29.00% of Python3 online submissions for Network Delay Time.
Memory Usage: 19.62 MB, less than 77.88% of Python3 online submissions for Network Delay Time.
"""
# Dijkstra with minHeap approach
# TC: O((v + e) * log(v)), SC: O(v + e)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = defaultdict(list)
        for i, time in enumerate(times):
            u, v, w = time
            adjMap[u].append((v, w))
            
        minHeap = [(0, k)]
        visited = set()
        res = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)
            
            res = time

            for nei, weight in adjMap[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + weight, nei))

        return res if len(visited) == n else -1



"""
Runtime: 4513 ms, faster than 5.01% of Python3 online submissions for Network Delay Time.
Memory Usage: 22.79 MB, less than 7.43% of Python3 online submissions for Network Delay Time.
"""
# DFS approach
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = defaultdict(list)
        timeMap = {}
        arrTime = {}
        for time in times:
            u, v, w = time
            adjMap[u].append(v)
            timeMap[(u, v)] = w

        arrTime = {i: float("inf") for i in range(1, n + 1)}
        arrTime[k] = 0

        def dfs(node, curTime):
            for nei in adjMap[node]:
                newTime = curTime + timeMap[(node, nei)]
                if newTime < arrTime[nei]:
                    arrTime[nei] = newTime
                    dfs(nei, newTime)

        dfs(k, 0)
        
        res = max(arrTime.values())
        return res if res < float("inf") else - 1