"""
Accepted
617 [Easy]
Runtime: 54 ms, faster than 48.45% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 18.78 MB, less than 72.67% of Python3 online submissions for Merge Two Binary Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1 or not root2:
            if root1:
                return TreeNode(root1.val, self.mergeTrees(root1.left, None), self.mergeTrees(root1.right, None))
            else:
                return TreeNode(root2.val, self.mergeTrees(root2.left, None), self.mergeTrees(root2.right, None))
        else:
            newNode = TreeNode(root1.val + root2.val)
            newNode.left = self.mergeTrees(root1.left, root2.left)
            newNode.right = self.mergeTrees(root1.right, root2.right)

            return newNode