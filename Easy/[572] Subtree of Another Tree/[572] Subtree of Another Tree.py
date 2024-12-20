"""
Accepted
572 [Easy]
Runtime: 47 ms, faster than 34.44% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 18.34 MB, less than 8.78% of Python3 online submissions for Subtree of Another Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(p, q):
            if not p and not q:
                return True

            if p and not q or q and not p:
                return False

            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)