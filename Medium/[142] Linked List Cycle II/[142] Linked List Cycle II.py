"""
Accepted
142 [Medium]
Runtime: 42 ms, faster than 67.76% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 19.56 MB, less than 8.09% of Python3 online submissions for Linked List Cycle II.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set()
        ptr = head
        while ptr:
            if ptr in hashSet:
                return ptr
            hashSet.add(ptr)
            ptr = ptr.next
        return None