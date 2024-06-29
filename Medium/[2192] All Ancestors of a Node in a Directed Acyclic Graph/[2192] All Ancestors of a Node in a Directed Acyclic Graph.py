"""
Accepted
2192 [Medium]
Runtime: 601 ms, faster than 37.65% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
Memory Usage: 51.20 MB, less than 19.58% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
"""
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        for nodeA, nodeB in edges:
            adjList[nodeB].append(nodeA)

        ancestors = [set() for _ in range(n)]
        for node in range(n):
            queue = deque([node])
            visited = set()

            while queue:
                cur = queue.popleft()
                for neighbor in adjList[cur]:
                    if neighbor not in visited:
                        ancestors[node].add(neighbor)
                        visited.add(neighbor)
                        queue.append(neighbor)

        return [sorted(list(s)) for s in ancestors]