"""
Accepted
104 [Easy]
Runtime: 30 ms, faster than 97.72% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 17.51 MB, less than 89.59% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res

        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res += 1
            queue = temp
        
        return res