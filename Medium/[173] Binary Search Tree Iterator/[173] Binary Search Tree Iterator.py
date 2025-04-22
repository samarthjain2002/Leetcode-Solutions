"""
Accepted
173 [Medium]
Runtime: 10 ms, faster than 38.85% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 25.08 MB, less than 57.73% of Python3 online submissions for Binary Search Tree Iterator.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)
        
        inorder(root)

        self.ptr = 0

    def next(self) -> int:
        res = self.arr[self.ptr]
        self.ptr += 1
        return res

    def hasNext(self) -> bool:
        return self.ptr < len(self.arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()