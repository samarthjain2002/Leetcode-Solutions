"""
Accepted
1038 [Medium]
Runtime: 37 ms, faster than 52.42% of Python online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 16.44 MB, less than 74.62% of Python online submissions for Binary Search Tree to Greater Sum Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = 0
        def reverseInOrder(root):
            nonlocal sum
            if root:
                reverseInOrder(root.right)
                sum += root.val
                root.val = sum
                reverseInOrder(root.left)
        reverseInOrder(root)
        return root