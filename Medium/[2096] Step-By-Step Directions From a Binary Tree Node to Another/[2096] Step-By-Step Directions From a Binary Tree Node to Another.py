"""
Accepted
2096 [Medium]
Runtime: 292 ms, faster than 58.39% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another
Memory Usage:  53.26 MB, less than 34.23% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, target):
            if not node:
                return
            if node.val == target:
                return path
            
            path.append('L')
            res = dfs(node.left, path, target)
            if res:
                return res

            path.pop()
            path.append('R')
            res = dfs(node.right, path, target)
            if res:
                return res

            path.pop()
            return ""
        
        startPath = dfs(root, [], startValue)
        destPath = dfs(root, [], destValue)
        print(startPath, destPath)
        i = 0
        while i < min(len(startPath), len(destPath)) and startPath[i] == destPath[i]:
            i += 1

        return ''.join((['U'] * (len(startPath) - i)) + (destPath[i : ]))