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