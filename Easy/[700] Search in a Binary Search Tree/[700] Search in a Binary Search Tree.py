"""
Accepted
700 [Easy]
Runtime: 50 ms, faster than 85.33% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 18.33 MB, less than 29.71% of Python3 online submissions for Search in a Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val < root.val:
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root