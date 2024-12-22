"""
Accepted
1448 [Medium]
Runtime: 179 ms, faster than 5.18% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 21.04 MB, less than 5.65% of Python3 online submissions for Kth Smallest Element in a BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def dfs(node):
            nonlocal k, res
            if not node:
                return

            dfs(node.left)
            if k == 1:
                res = node.val
            k -= 1
            # If k == 0, we have found the kth smallest element, so no need of traversing anymore
            if k > 0:
                dfs(node.right)

        dfs(root)
        return res