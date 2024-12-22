"""
Accepted
105 [Medium]
Runtime: 91 ms, faster than 55.62% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 89.24 MB, less than 6.03% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])
        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])

        return root



"""
If you had trouble solving this problem, I would recommend you to watch the video explanation by [Neetcode](https://youtu.be/ihj4IQGZ2zc?si=NAT9m-7KVWuBjupD).

Follow up: If the Binary Tree had duplicate values (i.e, if different nodes in the tree have the same value), how would you solve this problem?
"""