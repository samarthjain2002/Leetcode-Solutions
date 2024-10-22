"""
Accepted
2583 [Medium]
Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Kth Largest Sum in a Binary Tree.
Memory Usage: 52.92 MB, less than 15.99% of Python3 online submissions for Kth Largest Sum in a Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSums = [root.val]

        queue = deque([root])
        while queue:
            levelSum = 0
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                    levelSum += node.left.val
                if node.right:
                    temp.append(node.right)
                    levelSum += node.right.val
            if levelSum:
                levelSums.append(levelSum)
            queue = temp
        
        if len(levelSums) < k:
            return -1
        else:
            levelSums.sort()
            return levelSums[-k]