"""
Accepted
210 [Medium]
Runtime: 7 ms, faster than 32.56% of Python3 online submissions for Course Schedule II.
Memory Usage: 19.78 MB, less than 5.73% of Python3 online submissions for Course Schedule II.
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adjMap = defaultdict(list)
        for a, b in prerequisites:
            adjMap[a].append(b)

        visited, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for crs in adjMap[course]:
                if not dfs(crs):
                    return False
            cycle.remove(course)
            visited.add(course)

            res.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res