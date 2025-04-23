"""
Accepted
106 [Medium]
Runtime: 3 ms, faster than 86.44% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 19.32 MB, less than 75.07% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {node: idx for idx, node in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return

            root = TreeNode(postorder.pop())

            idx = inorderIdx[root.val]

            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)



"""
Runtime: 68 ms, faster than 39.68% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 54.15 MB, less than 37.70% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
            
        root = TreeNode(postorder.pop())

        idx = inorder.index(root.val)

        root.right = self.buildTree(inorder[idx + 1 : ], postorder)
        root.left = self.buildTree(inorder[ : idx], postorder)

        return root