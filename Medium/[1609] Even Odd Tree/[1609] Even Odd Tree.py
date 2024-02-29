"""
Accepted
1609 [Medium]
Runtime: 223 ms, faster than 66.05% of Python3 online submissions for Even Odd Tree.
Memory Usage: 37.85 MB, less than 66.05% of Python3 online submissions for Even Odd Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        def checkOrder(tempLevel, incOrder):
            N = len(tempLevel)
            if incOrder:
                if tempLevel[0] % 2 == 0:
                    return False
                for i in range(1, N):
                    if tempLevel[i - 1] >= tempLevel[i] or tempLevel[i] % 2 == 0:
                        return False
            else:
                if tempLevel[0] % 2 != 0:
                    return False
                for i in range(1, N):
                    if tempLevel[i - 1] <= tempLevel[i] or tempLevel[i] % 2 != 0:
                        return False
            return True

        if not checkOrder([root.val], True):
            return False
        queue = [root]
        incOrder = False
        while queue:
            temp = []
            tempLevel = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                    tempLevel.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    tempLevel.append(node.right.val)
            if temp:
                queue = temp
                if not checkOrder(tempLevel, incOrder):
                    return False
                incOrder = not incOrder
            else:
                break

        return True