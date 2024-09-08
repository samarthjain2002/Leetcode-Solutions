"""
Accepted
1367 [Medium]
Runtime: 67 ms, faster than 58.24% of Python3 online submissions for Linked List in Binary Tree.
Memory Usage:  17.22 MB, less than 63.38% of Python3 online submissions for Linked List in Binary Tree.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(trNode, curNode):
            if not curNode:
                return True
            if not trNode:
                return
            if trNode.val == curNode.val:
                return dfs(trNode.left, curNode.next) or dfs(trNode.right, curNode.next)
            return False

        def checkPath(trNode):
            if not trNode:
                return False
            return dfs(trNode, head) or checkPath(trNode.left) or checkPath(trNode.right)

        return checkPath(root)