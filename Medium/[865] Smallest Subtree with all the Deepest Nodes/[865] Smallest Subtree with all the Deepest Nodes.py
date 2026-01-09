"""
Accepted
865 [Medium]
Runtime: 1 ms, faster than 24.73% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
Memory Usage: 19.52 MB, less than 11.50% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0 , None

            h1, n1 = dfs(node.left)
            h2, n2 = dfs(node.right)

            if h1 == h2:
                return h1 + 1, node
            elif h1 > h2:
                return h1 + 1, n1
            else:
                return h2 + 1, n2

        return dfs(root)[1]