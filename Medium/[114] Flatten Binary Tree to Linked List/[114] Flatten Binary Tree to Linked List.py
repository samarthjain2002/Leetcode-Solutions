"""
Accepted
114 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 18.10 MB, less than 26.10% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return

            leftTail = helper(node.left)
            rightTail = helper(node.right)

            if node.left:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            last = rightTail or leftTail or node
            return last

        helper(root)