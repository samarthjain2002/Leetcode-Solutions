"""
Accepted
116 [Medium]
Runtime: 47 ms, faster than 70.02% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage:  18.14 MB, less than 40.12% of Python3 online submissions for Populating Next Right Pointers in Each Node.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                N = len(temp)
                for i in range(N - 1):
                    temp[i].next = temp[i + 1]
                queue = temp
            else:
                break

        return root