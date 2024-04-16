"""
Accepted
623 [Medium]
Runtime: 53 ms, faster than 15.75% of Python3 online submissions for Add One Row to Tree.
Memory Usage:  17.76 MB, less than 73.75% of Python3 online submissions for Add One Row to Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root)
            return node
    
        queue = [root]
        for i in range(depth - 2):
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp

        for node in queue:
            temp = TreeNode(val, node.left)
            temp1 = TreeNode(val, None, node.right)
            node.left = temp
            node.right = temp1

        return root