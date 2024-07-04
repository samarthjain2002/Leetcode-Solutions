"""
Accepted
2181 [Medium]
Runtime: 791 ms, faster than 88.50% of Python3 online submissions for Merge Nodes in Between Zeros.
Memory Usage: 56.10 MB, less than 77.54% of Python3 online submissions for Merge Nodes in Between Zeros.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        cur = head
        ptr = cur.next
        while ptr:
            if ptr.val != 0:
                cur.val += ptr.val
                ptr = ptr.next
                cur.next = ptr
            else:
                if not ptr.next:
                    cur.next = None
                    return head
                cur = ptr
                ptr = ptr.next
        return head