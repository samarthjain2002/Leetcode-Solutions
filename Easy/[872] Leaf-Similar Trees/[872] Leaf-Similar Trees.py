"""
Accepted
872 [Easy]
Runtime: 29 ms, faster than 96.99% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 17.47 MB, less than 7.47% of Python3 online submissions for Leaf-Similar Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1, r2 = [], []
        def in_order_tree1(node, r):
            if node:
                if node.left == None and node.right == None:
                    r.append(node.val)
                in_order_tree1(node.left, r)
                in_order_tree1(node.right, r)

        in_order_tree1(root1, r1)
        in_order_tree1(root2, r2)

        if r1 == r2:
            return True
        else:
            return False