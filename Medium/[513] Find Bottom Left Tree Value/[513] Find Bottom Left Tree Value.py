"""
Accepted
513 [Medium]
Runtime: 11 ms, faster than 63.70% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage:  18.36 MB, less than 52.22% of Python3 online submissions for Find Bottom Left Tree Value.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            res = queue[0].val
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp

        return res