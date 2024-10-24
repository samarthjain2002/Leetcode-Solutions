"""
Accepted
951 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Flip Equivalent Binary Trees.
Memory Usage: 16.59 MB, less than 57.29% of Python3 online submissions for Flip Equivalent Binary Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val != root2.val:
            return False

        def dfs(node1, node2):
            # Both have children
            if node1.left and node1.right and node2.left and node2.right:
                if node1.left.val == node2.left.val and node1.right.val == node2.right.val:
                    return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
                elif node1.left.val == node2.right.val and node1.right.val == node2.left.val:
                    return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
                else:
                    return False
            # Neither have children
            elif not node1.left and not node1.right and not node2.left and not node2.right:
                return True
            # One has 1 or 2 children, the other doesn't
            elif ((node1.left or node1.right) and not node2.left and not node2.right) or ((node2.left or node2.right) and not node1.left and not node1.right):
                return False
            # One has both children, the other has only 1
            elif (node1.left and node1.right) and ((not node2.left and node2.right) or (not node2.right and node2.left)) or (node2.left and node2.right) and ((not node1.left and node1.right) or (not node1.right and node1.left)):
                return False
            # Both have 1 children
            else:
                if node1.left and node2.left and node1.left.val == node2.left.val:
                    return dfs(node1.left, node2.left)
                elif node1.left and node2.right and node1.left.val == node2.right.val:
                    return dfs(node1.left, node2.right)
                elif node1.right and node2.left and node1.right.val == node2.left.val:
                    return dfs(node1.right, node2.left)
                elif node1.right and node2.right and node1.right.val == node2.right.val:
                    return dfs(node1.right, node2.right)
                else:
                    return False

        return dfs(root1, root2)