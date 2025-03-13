"""
Accepted
1008 [Medium]
Runtime: 2 ms, faster than 25.18% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
Memory Usage: 17.73 MB, less than 67.69% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def insertNode(root, node):
            if node < root.val:
                if not root.left:
                    root.left = TreeNode(node)
                else:
                    insertNode(root.left, node)
            else:
                if not root.right:
                    root.right = TreeNode(node)
                else:
                    insertNode(root.right, node)
        
        for node in preorder[1 : ]:
            insertNode(root, node)
        return root