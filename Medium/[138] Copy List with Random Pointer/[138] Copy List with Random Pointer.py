"""
Accepted
138 [Medium]
Runtime: 36 ms, faster than 71.92% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage:  18.24 MB, less than 5.22% of Python3 online submissions for Copy List with Random Pointer.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        ptr1 = head
        newHead = Node(head.val)
        ptr2 = newHead
        node_copies = {head: newHead}
        while ptr1.next:
            newNode = Node(ptr1.next.val)
            node_copies[ptr1.next] = newNode

            ptr2.next = newNode
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = None

        ptr = head
        while ptr:
            if ptr.random:
                node_copies[ptr].random = node_copies[ptr.random]
            else:
                node_copies[ptr].random = None
            ptr = ptr.next
        return newHead