"""
Accepted
1377 [Hard]
Runtime: 88 ms, faster than 39.09% of Python3 online submissions for Frog Position After T Seconds.
Memory Usage: 16.73 MB, less than 55.91% of Python3 online submissions for Frog Position After T Seconds.
"""
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        visited = {1}
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(vertex, t, res):
            if vertex == target:
                count = sum(1 for child in adjList[vertex] if child not in visited)
                if count == 0 or t == 0:
                    return res
                else:
                    return 0
            if t == 0:
                return 0

            count = sum(1 for child in adjList[vertex] if child not in visited)
            
            if count == 0:
                return 0

            for child in adjList[vertex]:
                if child not in visited:
                    visited.add(child)
                    result = dfs(child, t - 1, res / count)
                    if result != 0:
                        return result
                    visited.remove(child)
            return 0
        
        return dfs(1, t, 1)