"""
Accepted
110 [Easy]
Runtime: 45 ms, faster than 59.68% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 17.78 MB, less than 11.60% of Python3 online submissions for Balanced Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True

            leftHeight, leftBalanced = dfs(node.left)
            rightHeight, rightBalanced = dfs(node.right)

            height = max(leftHeight, rightHeight) + 1
            isBalanced = leftBalanced and rightBalanced and (abs(rightHeight - leftHeight) <= 1)

            return height, isBalanced

        notnecessary, isBalanced = dfs(root)
        return isBalanced