"""
Accepted
938 [Easy]
Runtime: 133 ms, faster than 85.03% of Python3 online submissions for Range Sum of BST.
Memory Usage: 24.46 MB, less than 87.42% of Python3 online submissions for Range Sum of BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        count = 0
        def in_order_traversal(node):
            nonlocal count
            if node:
                in_order_traversal(node.left)
                if node.val >= low and node.val <= high:
                    count += node.val
                in_order_traversal(node.right)
        in_order_traversal(root)

        return count