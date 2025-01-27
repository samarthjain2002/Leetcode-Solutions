"""
Accepted
1462 [Medium]
Runtime: 67 ms, faster than 49.56% of Python online submissions for Course Schedule IV.
Memory Usage: 20.66 MB, less than 43.44% of Python online submissions for Course Schedule IV.
"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        for prereq in prerequisites:
            a, b = prereq[0], prereq[1]
            adjList[b].append(a)

        prereqMap = defaultdict(set)
        def dfs(course):
            if course not in prereqMap:
                for prereq in adjList[course]:
                    prereqMap[course] = prereqMap[course] | dfs(prereq)
            return prereqMap[course] | {course}

        for course in range(numCourses):
            dfs(course)

        res = []
        for query in queries:
            u, v = query[0], query[1]
            res.append(u in prereqMap[v])
        return res



"""
Runtime: 57 ms, faster than 52.39% of Python online submissions for Course Schedule IV.
Memory Usage: 20.55 MB, less than 34.22% of Python online submissions for Course Schedule IV.
"""
from collections import deque, defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # Initialize adjacency list and reachable matrix
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # Build the isReachable matrix
        isReachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Perform BFS from each course
        for course in range(numCourses):
            queue = deque([course])
            visited = set()
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        isReachable[course][neighbor] = True
                        queue.append(neighbor)
        
        # Answer each query
        result = []
        for u, v in queries:
            result.append(isReachable[u][v])
        
        return result