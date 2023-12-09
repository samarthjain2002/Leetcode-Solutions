"""
Accepted
94 [Easy]
Runtime: 47 ms, faster than 8.14% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 16.50 MB, less than 19.15% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorderTraversal(root):
            if root:
                inorderTraversal(root.left)
                res.append(root.val)
                inorderTraversal(root.right)
        inorderTraversal(root)
        return res