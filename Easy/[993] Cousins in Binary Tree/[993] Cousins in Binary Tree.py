"""
Accepted
993 [Easy]
Runtime: 7 ms, faster than 92.79% of Python3 online submissions for Cousins in Binary Tree.
Memory Usage: 16.82 MB, less than 6.72% of Python3 online submissions for Cousins in Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False

        queue = [root]
        enc = False
        while queue:
            temp = []
            for node in queue:
                if node.left and node.right:
                    if (node.left.val == x or node.left.val == y) and (node.right.val == x or node.right.val == y):
                        return False
                if node.left:
                    if (node.left.val == x or node.left.val == y):
                        if enc:
                            return True
                        else:
                            enc = True
                    temp.append(node.left)
                if node.right:
                    if (node.right.val == x or node.right.val == y):
                        if enc:
                            return True
                        else:
                            enc = True
                    temp.append(node.right)
            if enc:
                return False
            print(temp)
            queue = temp