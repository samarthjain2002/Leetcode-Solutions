"""
Accepted
143 [Medium]
Runtime: 53 ms, faster than 71.33% of Python3 online submissions for Reorder List.
Memory Usage:  24.58 MB, less than 87.25% of Python3 online submissions for Reorder List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def split(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            reversedList = reverse(slow.next)
            slow.next = None
            return head, reversedList

        def reverse(head):
            if head == None or head.next == None:
                return head
            p = reverse(head.next)
            head.next.next = head
            head.next = None
            return p

        left, right = split(head)
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2