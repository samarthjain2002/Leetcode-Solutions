"""
Accepted
653 [Medium]
Runtime: 70 ms, faster than 56.28% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage:  18.29 MB, less than 99.57% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        numbers = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            numbers.append(node.val)
            inOrder(node.right)
        inOrder(root)

        left, right = 0, len(numbers) - 1
        while left != right:
            if numbers[left] + numbers[right] == k:
                return True
            elif numbers[left] + numbers[right] > k:
                right -= 1
            else:
                left += 1
        return False