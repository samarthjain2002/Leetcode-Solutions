"""
Accepted
2095 [Medium]
Runtime: 92 ms, faster than 53.17% of Python3 online submissions for Delete the Middle Node of a Linked List.
Memory Usage: 62.44 MB, less than 28.88% of Python3 online submissions for Delete the Middle Node of a Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Only 1 node
        if not head.next:
            return None

        # Floyd's tortoise and hare algorithm
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        slow.next = slow.next.next
        return head