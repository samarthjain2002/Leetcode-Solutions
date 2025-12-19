"""
Accepted
2092 [Hard]
Runtime: 381 ms, faster than 36.95% of Python3 online submissions for Find All People With Secret.
Memory Usage: 80.96 MB, less than 6.37% of Python3 online submissions for Find All People With Secret.
"""
# DFS Solution
# TC: O(mlogm + nm), SC: O(m + n)
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        aware = set([0, firstPerson])

        timeMap = {}
        for x, y, t in meetings:
            if t not in timeMap:
                timeMap[t] = defaultdict(list)
            timeMap[t][x].append(y)
            timeMap[t][y].append(x)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            aware.add(node)
            for nei in adjMap[node]:
                dfs(nei)

        meetingTimes = sorted(timeMap.keys())
        for t in meetingTimes:
            visited = set()
            adjMap = timeMap[t]
            for src in timeMap[t]:
                if src in aware:
                    dfs(src)

        return list(aware)