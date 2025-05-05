"""
Accepted
1325 [Medium]
Runtime: 3 ms, faster than 42.64% of Python3 online submissions for Delete Leaves With a Given Value.
Memory Usage: 18.16 MB, less than 94.71% of Python3 online submissions for Delete Leaves With a Given Value.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            else:
                return node


        return dfs(root)