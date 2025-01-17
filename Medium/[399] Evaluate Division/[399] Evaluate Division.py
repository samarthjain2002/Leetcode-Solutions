"""
Accepted
399 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Evaluate Division.
Memory Usage: 17.74 MB, less than 49.76% of Python3 online submissions for Evaluate Division.
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            adjMap[a].append([b, values[i]])
            adjMap[b].append([a, 1 / values[i]])

        def bfs(source, target):
            if source not in adjMap or target not in adjMap:
                return -1

            queue, visited = deque(), set()
            queue.append([source, 1])
            while queue:
                node, weight = queue.popleft()
                if node == target:
                    return weight
                for nei, w in adjMap[node]:
                    if nei not in visited:
                        queue.append([nei, w * weight])
                        visited.add(nei)
            return -1

        return [bfs(query[0], query[1]) for query in queries]