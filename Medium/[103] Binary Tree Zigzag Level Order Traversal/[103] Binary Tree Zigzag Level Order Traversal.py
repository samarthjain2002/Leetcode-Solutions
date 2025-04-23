"""
Accepted
103 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage:  17.85 MB, less than 95.56% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        ltr = True

        while queue:
            res.append([])
            if ltr:
                for node in queue:
                    res[-1].append(node.val)
            else:
                for node in reversed(queue):
                    res[-1].append(node.val)

            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ltr = not ltr
        return res