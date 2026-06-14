"""
Accepted
2130 [Medium]
Runtime: 99 ms, faster than 11.12% of Python3 online submissions for Maximum Twin Sum of a Linked List.
Memory Usage: 66.31 MB, less than 5.03% of Python3 online submissions for Maximum Twin Sum of a Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive Solution
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def pairSum(self, head: Optional[ListNode]) -> int:
        # Count the number of nodes
        n = 0
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next

        ptr = head
        for i in range(n // 2 - 1):
            ptr = ptr.next

        # Reverse the second half
        ptr.next = self.reverseList(ptr.next)
        ptr = ptr.next

        res = 0
        cur = head
        while ptr:
            res = max(res, cur.val + ptr.val)
            cur = cur.next
            ptr = ptr.next
        return res