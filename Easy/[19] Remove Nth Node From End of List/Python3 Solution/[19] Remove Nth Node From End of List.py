"""
Accepted
19 [Easy]
Runtime: 39 ms, faster than 44.21% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 16.51 MB, less than 61.49% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        while ptr:
            count += 1
            ptr = ptr.next
        
        pn = count - n
        ptr, cur = head, head
        for i in range(pn):
            if i > 0:
                cur = cur.next
            ptr = ptr.next

        if ptr == head:
            head = head.next
            ptr = ptr.next
        else:
            cur.next = ptr.next
        
        return head