"""
Accepted
199 [Medium]
Runtime: 38 ms, faster than 46.19% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 16.60 MB, less than 21.35% of Python3 online submissions for Binary Tree Right Side View.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque([root])
        RSView = []
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            RSView.append(queue[-1].val)
            queue = temp
        return RSView