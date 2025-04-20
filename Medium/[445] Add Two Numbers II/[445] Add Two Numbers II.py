"""
Accepted
445 [Medium]
Runtime: 7 ms, faster than 45.85% of Python3 online submissions for Add Two Numbers II.
Memory Usage: 18.05 MB, less than 16.64% of Python3 online submissions for Add Two Numbers II.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        
        carry = 0
        result = None
        while stack1 or stack2:
            a = b = 0
            if stack1:
                a = stack1.pop()
            if stack2:
                b = stack2.pop()

            total = a + b + carry
            temp = ListNode(total % 10)
            carry = total // 10

            if not result:
                result = temp
            else:
                temp.next = result
                result = temp

        if carry:
            temp = ListNode(carry, result)
            result = temp

        return result