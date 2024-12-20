"""
Accepted
102 [Medium]
Runtime: 29 ms, faster than 9.23% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage:  17.21 MB, less than 87.55% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            res.append(tempLevel)
            queue = temp

        return res[:-1]