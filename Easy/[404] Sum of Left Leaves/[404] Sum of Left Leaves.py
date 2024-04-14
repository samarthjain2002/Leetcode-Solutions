"""
Accepted
404 [Easy]
Runtime: 37 ms, faster than 51.05% of Python online submissions for Sum of Left Leaves.
Memory Usage: 16.74 MB, less than 47.79% of Python online submissions for Sum of Left Leaves.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        res = 0
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return res