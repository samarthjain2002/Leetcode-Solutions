"""
Accepted
743 [Medium]
Runtime: 4513 ms, faster than 5.01% of Python3 online submissions for Network Delay Time.
Memory Usage: 22.79 MB, less than 7.43% of Python3 online submissions for Network Delay Time.
"""
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