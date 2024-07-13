"""
Accepted
1161 [Medium]
Runtime: 151 ms, faster than 67.39% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
Memory Usage: 20.09 MB, less than 16.90% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        sumValues = []
        while queue:
            temp = []
            s = 0
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                s += node.val
            sumValues.append(s)
            queue = temp
            
        maximal = 1
        for i, s in enumerate(sumValues):
            if s > sumValues[maximal - 1]:
                maximal = i + 1
        return maximal