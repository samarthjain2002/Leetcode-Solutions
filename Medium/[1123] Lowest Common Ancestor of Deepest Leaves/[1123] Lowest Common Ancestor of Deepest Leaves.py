"""
Accepted
1123 [Medium]
Runtime: 3 ms, faster than 57.53% of Python3 online submissions for Lowest Common Ancestor of Deepest Leaves.
Memory Usage: 18.31 MB, less than 25.86% of Python3 online submissions for Lowest Common Ancestor of Deepest Leaves.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (None, 0)

            leftLCA, leftHeight = dfs(node.left)
            rightLCA, rightHeight = dfs(node.right)

            if leftHeight == rightHeight:
                return node, leftHeight + 1
            elif leftHeight > rightHeight:
                return leftLCA, leftHeight + 1
            else:
                return rightLCA, rightHeight + 1

        LCA, _ = dfs(root)
        return LCA
