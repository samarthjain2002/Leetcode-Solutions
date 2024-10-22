"""
Accepted
590 [Easy]
Runtime: 36 ms, faster than 96.22% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 16.76 MB, less than 6.46% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            for n in node.children:
                dfs(n)
            res.append(node.val)

        dfs(root)
        return res