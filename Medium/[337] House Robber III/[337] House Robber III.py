"""
Accepted
337 [Medium]
Runtime: 42 ms, faster than 91.40% of Python3 online submissions for House Robber III.
Memory Usage:  18.05 MB, less than 100.00% of Python3 online submissions for House Robber III.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
            
        return max(dfs(root))