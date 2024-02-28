"""
Accepted
100 [Easy]
Runtime: 36 ms, faster than 52.39% of Python3 online submissions for Same Tree.
Memory Usage: 16.52 MB, less than 70.01% of Python3 online submissions for Same Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return []
            queue = [root]
            res = [root.val]
            while queue:
                temp = []
                for node in queue:
                    if node.left:
                        temp.append(node.left)
                        res.append(node.left.val)
                    else:
                        res.append(None)
                    if node.right:
                        temp.append(node.right)
                        res.append(node.right.val)
                    else:
                        res.append(None)
                queue = temp
            return res

        pTree = bfs(p)
        qTree = bfs(q)

        if pTree == qTree:
                return True
        else:
            return False