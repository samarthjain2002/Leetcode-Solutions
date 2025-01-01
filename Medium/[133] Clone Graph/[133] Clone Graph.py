"""
Accepted
133 [Medium]
Runtime: 46 ms, faster than 21.64% of Python3 online submissions for Clone Graph.
Memory Usage: 18.07 MB, less than 14.03% of Python3 online submissions for Clone Graph.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        elif not node.neighbors:
            return Node(node.val)

        visited = set()
        adjMap = defaultdict(list)
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbor in node.neighbors:
                adjMap[node.val].append(neighbor.val)
                dfs(neighbor)

        dfs(node)

        nodeMap = {}
        for key in adjMap.keys():
            newNode = Node(key)
            nodeMap[key] = newNode

        for key, values in adjMap.items():
            for val in values:
                nodeMap[key].neighbors.append(nodeMap[val])

        return nodeMap[1]