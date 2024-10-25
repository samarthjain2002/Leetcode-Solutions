"""
Accepted
1339 [Medium]
Runtime: 108 ms, faster than 94.15% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
Memory Usage: 38.47 MB, less than 16.10% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, totalSum = 0):
            nonlocal res
            if not node:
                return 0

            if totalSum == 0:
                sumOfSubtree = node.val + dfs(node.left) + dfs(node.right)
            else:
                sumOfSubtree = node.val + dfs(node.left, totalSum) + dfs(node.right, totalSum)
            res = max(res, (totalSum - sumOfSubtree) * sumOfSubtree)
            return sumOfSubtree

        totalSum = dfs(root)
        dfs(root, totalSum)
        return res % (10**9 + 7)