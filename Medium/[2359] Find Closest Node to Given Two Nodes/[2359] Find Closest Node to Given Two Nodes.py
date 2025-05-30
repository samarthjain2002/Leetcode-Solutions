"""
Accepted
2359 [Easy]
Runtime: 285 ms, faster than 36.65% of Python3 online submissions for Find Closest Node to Given Two Nodes.
Memory Usage: 95.54 MB, less than 5.43% of Python3 online submissions for Find Closest Node to Given Two Nodes.
"""
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited = set()
        def dfs(node, dist, distances):
            if node in visited:
                return

            visited.add(node)
            distances[node] = dist
            if edges[node] != -1:
                dfs(edges[node], dist + 1, distances)

        
        distFromNode1 = {}
        dfs(node1, 0, distFromNode1)

        distFromNode2 = {}
        visited.clear()
        dfs(node2, 0, distFromNode2)

        res, distance = -1, float("inf")
        for node in sorted(distFromNode1.keys()):
            if node in distFromNode2 and max(distFromNode1[node], distFromNode2[node]) < distance:
                distance = max(distFromNode1[node], distFromNode2[node])
                res = node
        return res