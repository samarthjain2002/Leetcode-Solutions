"""
Accepted
2807 [Medium]
Runtime: 62 ms, faster than 88.69% of Python3 online submissions for Insert Greatest Common Divisors in Linked List.
Memory Usage: 19.64 MB, less than 36.27% of Python3 online submissions for Insert Greatest Common Divisors in Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ptr = head
        while ptr:
            if ptr.next:
                value = gcd(ptr.val, ptr.next.val)
                ptr.next = ListNode(value, ptr.next)
                ptr = ptr.next
            ptr = ptr.next

        return head