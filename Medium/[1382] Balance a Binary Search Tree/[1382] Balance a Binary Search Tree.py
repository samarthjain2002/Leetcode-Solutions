"""
Accepted
1382 [Medium]
Runtime: 205 ms, faster than 44.98% of Python3 online submissions for Balance a Binary Search Tree.
Memory Usage: 22.00 MB, less than 60.27% of Python3 online submissions for Balance a Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        A = []
        def inorder(root):
            nonlocal A
            if root:
                inorder(root.left)
                A.append(root.val)
                inorder(root.right)
        inorder(root)
        
        def build(i, j):
            if i > j:
                return None
            mid = (i + j) // 2
            root = TreeNode(A[mid], build(i, mid - 1), build(mid + 1, j))
            return root

        return build(0,len(A) - 1)