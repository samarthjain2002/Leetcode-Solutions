"""
Accepted
437 [Medium]
Runtime: 515 ms, faster than 9.55% of Python3 online submissions for Path Sum III.
Memory Usage: 18.07 MB, less than 50.05% of Python3 online submissions for Path Sum III.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        def helper(node, val):
            if not node:
                return

            if node.val + val == targetSum:
                self.res += 1

            helper(node.left, node.val + val)
            helper(node.right, node.val + val)


        def dfs(node):
            if not node:
                return
            
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res