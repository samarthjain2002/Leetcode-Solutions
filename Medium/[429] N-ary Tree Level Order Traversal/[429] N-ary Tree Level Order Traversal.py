"""
Accepted
429 [Medium]
Runtime: 45 ms, faster than 66.73% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 18.40 MB, less than 10.45% of Python3 online submissions for N-ary Tree Level Order Traversal.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            temp = []
            forRes = []
            for node in queue:
                forRes.append(node.val)
                for child in node.children:
                    temp.append(child)
            res.append(forRes)
            queue = temp
        return res