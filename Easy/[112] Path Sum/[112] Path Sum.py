"""
Accepted
112 [Easy]
Runtime: 47 ms, faster than 17.62% of Python3 online submissions for Path Sum.
Memory Usage:  17.37 MB, less than 63.24% of Python3 online submissions for Path Sum.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, s):
            if not node:
                return False
            s += node.val
            if not node.left and not node.right:
                return s == targetSum
            return dfs(node.left, s) or dfs(node.right, s)

        return dfs(root, 0)