"""
Accepted
889 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
Memory Usage: 18.01 MB, less than 10.17% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def dfs(node, preorder, postorder):
            if not preorder or not postorder:
                return

            if preorder[0] == postorder[-1]:
                node.left = TreeNode(preorder[0])

                dfs(node.left, preorder[1 : ], postorder[ : -1])
            else:
                node.left = TreeNode(preorder[0])
                node.right = TreeNode(postorder[-1])

                pos1 = preorder.index(node.right.val)
                pos2 = postorder.index(node.left.val)

                dfs(node.left, preorder[1 : pos1], postorder[ : pos2])
                dfs(node.right, preorder[pos1 + 1 : ], postorder[pos2 + 1 : -1])

        dfs(root, preorder[1 : ], postorder[ : -1])
        return root