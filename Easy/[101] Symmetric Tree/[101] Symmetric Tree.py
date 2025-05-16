"""
Accepted
101 [Easy]
Runtime: 34 ms, faster than 75.91% of Python3 online submissions for Symmetric Tree.
Memory Usage: 16.63 MB, less than 10.45% of Python3 online submissions for Symmetric Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS approach
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False

            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root.left, root.right)



"""
Runtime: 2 ms, faster than 10.09% of Python3 online submissions for Symmetric Tree.
Memory Usage: 17.74 MB, less than 83.63% of Python3 online submissions for Symmetric Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS approach
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # BFS approach
        queue = deque([root])
        while queue:
            left, right = 0, len(queue) - 1
            while left < right:
                if not queue[left] and not queue[right]:
                    pass
                elif not queue[left] or not queue[right]:
                    return False
                elif queue[left].val != queue[right].val:
                    return False
                left += 1
                right -= 1
            
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left if node.left else None)
                    queue.append(node.right if node.right else None)
        return True