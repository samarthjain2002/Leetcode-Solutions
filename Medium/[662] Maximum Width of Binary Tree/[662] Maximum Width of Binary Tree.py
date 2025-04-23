"""
Accepted
662 [Medium]
Runtime: 8 ms, faster than 11.49% of Python3 online submissions for Maximum Width of Binary Tree.
Memory Usage: 19.81 MB, less than 5.20% of Python3 online submissions for Maximum Width of Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        minimum = {}
        maximum = {}
        
        def dfs(node, pos, level):
            if not node:
                return

            minimum[level] = pos if level not in minimum else min(minimum[level], pos)
            maximum[level] = pos if level not in maximum else max(maximum[level], pos)

            dfs(node.left, pos + (pos - 1), level + 1)
            dfs(node.right, pos + pos, level + 1)
        
        dfs(root, 1, 0)

        res = float("-inf")
        for level in minimum.keys():
            res = max(res, maximum[level] - minimum[level] + 1)
        return res