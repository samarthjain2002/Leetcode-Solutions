"""
Accepted
226 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 17.68 MB, less than 5.36% of Python3 online submissions for Invert Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.left, node.right = node.right, node.left

            self.invertTree(node.left)
            self.invertTree(node.right)
        
        dfs(root)
        return root


"""
Runtime: 31 ms, faster than 100.00% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 16.53 MB, less than 83.44% of Python3 online submissions for Invert Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left and not root.right:
            return root
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root