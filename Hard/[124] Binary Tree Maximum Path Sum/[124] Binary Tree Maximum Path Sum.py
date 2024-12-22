"""
Accepted
124 [Hard]
Runtime: 12 ms, faster than 76.84% of Python3 online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 23.19 MB, less than 6.34% of Python3 online submissions for Binary Tree Maximum Path Sum.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            res = max(res, left + node.val + right)

            return node.val + max(left, right)

        dfs(root)
        return res