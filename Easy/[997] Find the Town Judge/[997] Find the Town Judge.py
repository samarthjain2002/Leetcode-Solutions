"""
Accepted
997 [Easy]
Runtime: 597 ms, faster than 97.60% of Python3 online submissions for Find the Town Judge.
Memory Usage: 22.63 MB, less than 6.44% of Python3 online submissions for Find the Town Judge.
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            if n == 1:
                return 1
            return -1

        adjList = defaultdict(list)
        for edge in trust:
            adjList[edge[1]].append(edge[0])
        
        trusters = set()
        for value in adjList.values():
            for val in value:
                trusters.add(val)

        for key, value in adjList.items():
            if len(value) == n - 1 and key not in trusters:
                return key
        return -1