"""
Accepted
1028 [Hard]
Runtime: 5 ms, faster than 100.00% of Python3 online submissions for Recover a Tree From Preorder Traversal.
Memory Usage: 18.04 MB, less than 99.71% of Python3 online submissions for Recover a Tree From Preorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        traversal += '-'

        stack = []
        
        dashCount = 0
        num = ""
        for char in traversal:
            if char.isdigit():
                num += char
            elif not num:
                dashCount += 1
            else:
                newNode = TreeNode(int(num))

                while len(stack) > dashCount:
                    stack.pop()

                if stack:
                    if stack[-1].left:
                        stack[-1].right = newNode
                        stack.append(newNode)
                    else:
                        stack[-1].left = newNode
                        stack.append(newNode)
                else:
                    stack.append(newNode)

                dashCount = 1
                num = ""

        return stack[0]