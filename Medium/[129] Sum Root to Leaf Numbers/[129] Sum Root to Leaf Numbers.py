"""
Accepted
129 [Medium]
Runtime: 29 ms, faster than 90.71% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage:  16.53 MB, less than 26.23% of Python3 online submissions for Sum Root to Leaf Numbers.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        count = ""
        res = 0

        def preOrder(node):
            if not node:
                return

            nonlocal res, count
            count += str(node.val)
            if not node.left and not node.right:
                res += int(count)

            preOrder(node.left)
            preOrder(node.right)

            count = count[: - 1]

        preOrder(root)
        
        return res