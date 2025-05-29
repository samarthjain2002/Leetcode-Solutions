"""
Accepted
3373 [Hard]
Runtime: 640 ms, faster than 22.73% of Python3 online submissions for Maximize the Number of Target Nodes After Connecting Trees II.
Memory Usage: 130.04 MB, less than 10.23% of Python3 online submissions for Maximize the Number of Target Nodes After Connecting Trees II.
"""
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        adjMap1 = defaultdict(list)
        for a, b in edges1:
            adjMap1[a].append(b)
            adjMap1[b].append(a)

        adjMap2 = defaultdict(list)
        for a, b in edges2:
            adjMap2[a].append(b)
            adjMap2[b].append(a)

        visited = set()
        def dfs(node, adjMap, black, white, blackNode):
            visited.add(node)

            if blackNode:
                black.add(node)
            else:
                white.add(node)

            for nei in adjMap[node]:
                if nei not in visited:
                    dfs(nei, adjMap, black, white, not blackNode)

        
        black1 = set()
        white1 = set()
        dfs(0, adjMap1, black1, white1, True)

        black2 = set()
        white2 = set()
        visited.clear()
        dfs(0, adjMap2, black2, white2, True)

        answer = []
        for i in range(len(adjMap1)):
            if i in black1:
                answer.append(len(black1) + max(len(black2), len(white2)))
            else:
                answer.append(len(white1) + max(len(black2), len(white2)))
        return answer