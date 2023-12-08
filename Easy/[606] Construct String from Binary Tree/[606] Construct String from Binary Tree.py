"""
Accepted
606 [Easy]
Runtime: 54 ms, faster than 48.45% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 18.78 MB, less than 72.67% of Python3 online submissions for Construct String from Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def PreorderTraversal(root):
            nonlocal res
            if root:
                res += "("
                res += str(root.val)
                if not root.left and root.right:
                    res += "()"
                PreorderTraversal(root.left)
                PreorderTraversal(root.right)
                res += ')'
            return res
        PreorderTraversal(root)
        return res[1:-1]