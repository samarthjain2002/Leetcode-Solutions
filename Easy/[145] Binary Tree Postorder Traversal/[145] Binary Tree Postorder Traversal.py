"""
Accepted
145 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 16.79 MB, less than 25.99% of Python3 online submissions for Binary Tree Postorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res