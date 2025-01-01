"""
Accepted
207 [Medium]
Runtime: 3 ms, faster than 88.97% of Python3 online submissions for Course Schedule.
Memory Usage: 19.13 MB, less than 17.49% of Python3 online submissions for Course Schedule.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for a, b in prerequisites:
            adjMap[a].append(b)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            elif not adjMap[course]:
                return True

            visited.add(course)
            for crs in adjMap[course]:
                if not dfs(crs):
                    return False
            visited.remove(course)
            adjMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True