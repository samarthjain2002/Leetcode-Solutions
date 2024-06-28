"""
Accepted
2285 [Medium]
Runtime: 1336 ms, faster than 20.08% of Python3 online submissions for Maximum Total Importance of Roads.
Memory Usage:  44.67 MB, less than 20.08% of Python3 online submissions for Maximum Total Importance of Roads.
"""
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for a, b in roads:
            adjList[a].append(b)
            adjList[b].append(a)

        freq = [[len(val), key] for key, val in adjList.items()]
        def custom_sort_condition(item):
            return -item[0],-len(adjList[item[1]])
        freq.sort(key = custom_sort_condition)
        
        valAssigned = {}
        for item in freq:
            valAssigned[item[1]] = n
            n -= 1

        res = 0
        for a, b in roads:
            res += valAssigned[a] + valAssigned[b]

        return res