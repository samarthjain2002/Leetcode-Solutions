"""
Accepted
1110 [Medium]
Runtime: 51 ms, faster than 80.33% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage:  17.13 MB, less than 7.26% of Python3 online submissions for Delete Nodes And Return Forest.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
            
        to_delete = set(to_delete)
        res_set = set([root])

        def dfs(node):
            if not node:
                return None

            res = node
            if node.val in to_delete:
                res = None
                res_set.discard(node)
                if node.left:
                    res_set.add(node.left)
                if node.right:
                    res_set.add(node.right)

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return res

        dfs(root)
        return list(res_set)