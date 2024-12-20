"""
Accepted
543 [Easy]
Runtime: 3 ms, faster than 95.08% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 20.96 MB, less than 6.00% of Python3 online submissions for Diameter of Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return -1

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            res = max(res, left + right)

            return max(left, right)

        dfs(root)
        return res