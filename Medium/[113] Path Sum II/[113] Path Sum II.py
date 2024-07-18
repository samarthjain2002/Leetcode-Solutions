"""
Accepted
113 [Medium]
Runtime: 45 ms, faster than 39.43% of Python3 online submissions for Path Sum II.
Memory Usage:  17.45 MB, less than 53.17% of Python3 online submissions for Path Sum II.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, s, temp):
            if not node:
                return None
            s += node.val
            temp.append(node.val)
            if not node.left and not node.right:
                if s == targetSum:
                    res.append(temp[:])
            else:
                dfs(node.left, s, temp)
                dfs(node.right, s, temp)
            temp.pop()

        dfs(root, 0, [])
        return res