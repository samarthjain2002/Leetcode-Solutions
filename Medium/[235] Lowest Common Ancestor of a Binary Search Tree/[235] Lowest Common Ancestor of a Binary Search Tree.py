"""
Accepted
235 [Easy]
Runtime: 42 ms, faster than 98.68% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree
Memory Usage: 20.88 MB, less than 16.96% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Wow since it is BST
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root


"""
Runtime: 62 ms, faster than 18.14% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree
Memory Usage: 21.18 MB, less than 6.78% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # This is more complicated for a more generic tree:
        def dfs(node):
            if not node or node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left or right

        return dfs(root)