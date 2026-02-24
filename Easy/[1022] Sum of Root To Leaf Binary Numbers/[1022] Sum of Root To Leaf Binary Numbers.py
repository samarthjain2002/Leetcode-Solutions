"""
Accepted
1022 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
Memory Usage: 19.53 MB, less than 56.83% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def trav(node, num):
            if not node.left and not node.right:
                num = num << 1
                num += node.val
                self.res += num
                return

            num = num << 1
            num += node.val
            if node.left:
                trav(node.left, num)
            if node.right:
                trav(node.right, num)

        trav(root, 0)
        return self.res