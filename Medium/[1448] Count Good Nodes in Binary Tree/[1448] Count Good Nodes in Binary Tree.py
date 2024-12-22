"""
Accepted
1448 [Medium]
Runtime: 179 ms, faster than 5.18% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 32.14 MB, less than 5.49% of Python3 online submissions for Count Good Nodes in Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        m = root.val
        res = 0
        def dfs(node, m):
            nonlocal res

            if not node:
                return

            if m <= node.val:
                res += 1
            m = max(m, node.val)

            dfs(node.left, m)
            dfs(node.right, m)

        dfs(root, m)
        return res