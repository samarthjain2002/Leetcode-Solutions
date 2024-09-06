"""
Accepted
3217 [Medium]
Runtime: 718 ms, faster than 62.33% of Python3 online submissions for Delete Nodes From Linked List Present in Array.
Memory Usage: 54.94 MB, less than 70.63% of Python3 online submissions for Delete Nodes From Linked List Present in Array.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head.val in nums:
            head = head.next
        cur, ptr = head, head.next

        while ptr:
            while ptr and ptr.val in nums:
                ptr = ptr.next
            cur.next = ptr
            if ptr:
                cur = ptr
                ptr = ptr.next
        return head