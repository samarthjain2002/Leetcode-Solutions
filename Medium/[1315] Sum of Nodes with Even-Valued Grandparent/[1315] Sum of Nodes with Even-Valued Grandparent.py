"""
Accepted
1315 [Medium]
Runtime: 64 ms, faster than 97.87% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 19.93 MB, less than 90.97% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum = 0
        def traversal(node):
            nonlocal sum
            if node:
                if node.val % 2 == 0:
                    if node.left != None:
                        if node.left.left != None:
                            sum += node.left.left.val
                        if node.left.right != None:
                            sum += node.left.right.val
                    if node.right != None:
                        if node.right.left != None:
                            sum += node.right.left.val
                        if node.right.right != None:
                            sum += node.right.right.val
                traversal(node.left)
                traversal(node.right)
        traversal(root)

        return sum