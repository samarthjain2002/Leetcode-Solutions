"""
Accepted
257 [Easy]
Runtime: 4 ms, faster than 2.30% of Java online submissions for Binary Tree Paths.
Memory Usage: 17.80 MB, less than 42.57% of Java online submissions for Binary Tree Paths.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(node, path):
            path.append(node.val)

            if not node.left and not node.right:
                res.append("->".join([str(node) for node in path]))
            if node.left:
                backtrack(node.left, path)
            if node.right:
                backtrack(node.right, path)
            path.pop()
            

        backtrack(root, [])
        return res