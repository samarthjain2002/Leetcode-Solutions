"""
Accepted
141 [Easy]
Runtime: 50 ms, faster than 46.76% of Python3 online submissions for Linked List Cycle.
Memory Usage: 19.85 MB, less than 58.28% of Python3 online submissions for Linked List Cycle.
"""
# TC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast, = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break

            if slow == fast:
                return True
        return False



"""
Runtime: 50 ms, faster than 24.76% of Python3 online submissions for Linked List Cycle.
Memory Usage: 19.66 MB, less than 6.16% of Python3 online submissions for Linked List Cycle.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# SC: O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        ptr = head
        while ptr:
            if ptr in hashSet:
                return True
            hashSet.add(ptr)
            ptr = ptr.next
        return False