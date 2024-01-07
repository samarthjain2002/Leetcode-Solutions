"""
Accepted
1971 [Easy]
Runtime: 1515 ms, faster than 86.80% of Python3 online submissions for Find if Path Exists in Graph.
Memory Usage: 109.63 MB, less than 52.27% of Python3 online submissions for Find if Path Exists in Graph.
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjList = defaultdict(list)
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            
        stack = [source]
        
        while len(stack) > 0:
            node = stack.pop()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for node in adjList[node]:
                stack.append(node)
                
        return False