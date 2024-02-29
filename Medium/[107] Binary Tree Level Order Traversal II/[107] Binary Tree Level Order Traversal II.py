"""
Accepted
107 [Medium]
Runtime: 25 ms, faster than 98.45% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage:  16.86 MB, less than 56.28% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = [[root.val]]
        while queue:
            temp = []
            tempLevel = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                    tempLevel.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    tempLevel.append(node.right.val)
            res = [tempLevel] + res
            queue = temp

        return res[1:]