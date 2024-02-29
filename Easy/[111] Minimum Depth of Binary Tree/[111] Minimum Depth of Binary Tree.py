"""
Accepted
111 [Easy]
Runtime: 200 ms, faster than 97.19% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 43.48 MB, less than 51.16% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res

        queue = [root]
        while queue:
            temp = []
            res += 1
            for node in queue:
                if not node.left and not node.right:
                    return res
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp