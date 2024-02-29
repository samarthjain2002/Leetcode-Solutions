"""
Accepted
637 [Easy]
Runtime: 46 ms, faster than 54.84% of Python online submissions for Average of Levels in Binary Tree.
Memory Usage: 18.26 MB, less than 98.78% of Python online submissions for Average of Levels in Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        res = [root.val]
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
            if tempLevel:
                res.append(sum(tempLevel) / len(tempLevel))
            queue = temp

        return res