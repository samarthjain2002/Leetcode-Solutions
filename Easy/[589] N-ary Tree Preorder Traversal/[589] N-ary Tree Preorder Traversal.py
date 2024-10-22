"""
Accepted
589 [Easy]
Runtime: 45 ms, faster than 59.73% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.76 MB, less than 6.46% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                return

            res.append(node.val)
            for n in node.children:
                dfs(n)

        dfs(root)
        return res