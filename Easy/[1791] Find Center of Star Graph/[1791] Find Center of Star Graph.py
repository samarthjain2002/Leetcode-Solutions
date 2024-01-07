"""
Accepted
1791 [Easy]
Runtime: 689 ms, faster than 90.16% of Python3 online submissions for Find Center of Star Graph.
Memory Usage: 54.76 MB, less than 5.15% of Python3 online submissions for Find Center of Star Graph.
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        NumOfEdges = len(edges)
        for key, value in adjList.items():
            if len(value) == NumOfEdges:
                return key