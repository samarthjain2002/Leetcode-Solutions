"""
Accepted
144 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 16.76 MB, less than 6.46% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            nonlocal res
            if not node:
                return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return res