"""
Accepted
108 [Easy]
Runtime: 5 ms, faster than 9.54% of Python online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 19.30 MB, less than 15.73% of Python online submissions for Convert Sorted Array to Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(low, high):
            if low > high:
                return None

            mid = low + ((high - low) // 2)

            node = TreeNode(nums[mid])
            node.left = dfs(low, mid - 1)
            node.right = dfs(mid + 1, high)

            return node

        
        return dfs(0, len(nums) - 1)