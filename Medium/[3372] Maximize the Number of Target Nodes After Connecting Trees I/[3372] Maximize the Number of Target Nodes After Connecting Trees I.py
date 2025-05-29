"""
Accepted
3372 [Medium]
Runtime: 2122 ms, faster than 28.80% of Python3 online submissions for Maximize the Number of Target Nodes After Connecting Trees I.
Memory Usage: 18.91 MB, less than 35.20% of Python3 online submissions for Maximize the Number of Target Nodes After Connecting Trees I.
"""
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adjMap1 = defaultdict(list)
        for a, b in edges1:
            adjMap1[a].append(b)
            adjMap1[b].append(a)

        adjMap2 = defaultdict(list)
        for a, b in edges2:
            adjMap2[a].append(b)
            adjMap2[b].append(a)

        answer = []
        visited = set()
        def dfs(node, adjMap, k):
            visited.add(node)

            if k:
                res = 1
                for nei in adjMap[node]:
                    if nei not in visited:
                        res += dfs(nei, adjMap, k - 1)
                return res
            else:
                return 0


        for i in range(len(adjMap1)):
            visited.clear()
            answer.append(dfs(i, adjMap1, k + 1))

        maxReachable = float("-inf")
        for i in range(len(adjMap2)):
            visited.clear()
            temp = dfs(i, adjMap2, k)
            maxReachable = max(maxReachable, temp)

        return [ans + maxReachable for ans in answer]