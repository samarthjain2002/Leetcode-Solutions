"""
Accepted
2196 [Medium]
Runtime: 1565 ms, faster than 64.65% of Python3 online submissions for Create Binary Tree From Descriptions.
Memory Usage: 25.72 MB, less than 85.86% of Python3 online submissions for Create Binary Tree From Descriptions.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashMap = {}
        for parent, child, isLeft in descriptions:
            if parent not in hashMap:
                hashMap[parent] = TreeNode(parent)
            if child not in hashMap:
                hashMap[child] = TreeNode(child)
            
            if isLeft:
                hashMap[parent].left = hashMap[child]
            else:
                hashMap[parent].right = hashMap[child]
        
        for parent, child, isLeft in descriptions:
            del hashMap[child]

        for val in hashMap.values():
            return val