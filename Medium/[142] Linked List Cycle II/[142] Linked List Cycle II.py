"""
Accepted
142 [Medium]
Runtime: 53 ms, faster than 18.77% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 19.67 MB, less than 54.56% of Python3 online submissions for Linked List Cycle II.
"""
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        # No cycle
        if not fast.next or not fast.next.next:
            return None

        # There definitely is a cycle
        slow2 = head
        while True:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next
        # No need to add a return sice there is a cycle



"""
Runtime: 42 ms, faster than 67.76% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 19.56 MB, less than 8.09% of Python3 online submissions for Linked List Cycle II.
"""
# SC: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set()
        ptr = head
        while ptr:
            if ptr in hashSet:
                return ptr
            hashSet.add(ptr)
            ptr = ptr.next
        return None