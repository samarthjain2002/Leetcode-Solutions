"""
Accepted
2385 [Medium]
Runtime: 439 ms, faster than 80.26% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
Memory Usage: 64.63MB, less than 64.43% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjList = defaultdict(list)
        count = 0 # Use a counter to track unique nodes
        def traversal(node, adjList):
            nonlocal count
            if node:
                count += 1  # Increment the counter
                if node.left:
                    adjList[node.val].append(node.left.val)
                    adjList[node.left.val].append(node.val)
                    traversal(node.left, adjList)
                if node.right:
                    adjList[node.val].append(node.right.val)
                    adjList[node.right.val].append(node.val)
                    traversal(node.right, adjList)
        traversal(root, adjList)
        
        infected = {start}
        mins = 0
        def bfs(adjList, startNode):
            nonlocal mins
            visited = {startNode}
            queue = []
            queue.append(startNode)
            
            while queue:
                size = len(queue)
                for i in range(size):
                    current = queue.pop(0)
                    for neighbor in adjList[current]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                if queue:  # Check if there are more nodes in the queue for the next level
                    mins += 1  # Increment time after processing all nodes at the current level
        bfs(adjList, start)
        
        return mins