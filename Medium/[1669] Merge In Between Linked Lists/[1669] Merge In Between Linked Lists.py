"""
Accepted
1669 [Medium]
Runtime: 191 ms, faster than 63.38% of Python3 online submissions for Merge In Between Linked Lists.
Memory Usage: 21.08 MB, less than 70.92% of Python3 online submissions for Merge In Between Linked Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr1, ptr2 = list1, list1
        while b >= 0:
            if a > 1:
                ptr1 = ptr1.next
                a -= 1
            ptr2 = ptr2.next
            b -= 1

        ptr1.next = list2
        while ptr1.next:
            ptr1 = ptr1.next
        ptr1.next = ptr2

        return list1