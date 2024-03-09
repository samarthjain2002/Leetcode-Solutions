"""
Accepted
206 [Easy]
Runtime: 42 ms, faster than 24.19% of Python3 online submissions for Reverse Linked List.
Memory Usage: 17.67 MB, less than 81.60% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive Solution
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p