"""
Accepted
83 [Easy]
Runtime: 42 ms, faster than 44.13% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 16.53 MB, less than 34.04% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        cur = head
        ptr = head.next
        while ptr:
            if cur.val == ptr.val:
                ptr = ptr.next
                cur.next = ptr
            else:
                ptr = ptr.next
                cur = cur.next
        return head