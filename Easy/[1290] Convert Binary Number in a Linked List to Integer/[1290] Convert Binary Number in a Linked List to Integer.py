"""
Accepted
1290 [Easy]
Runtime: 97 ms, faster than 39.02% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 17.61 MB, less than 77.66% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        bin_num = ""
        while head:
            bin_num += str(head.val)
            head = head.next

        res, exp = 0, 0
        for i in reversed(range(len(bin_num))):
            if bin_num[i] == '1':
                res += 2**exp
            exp += 1
        return res