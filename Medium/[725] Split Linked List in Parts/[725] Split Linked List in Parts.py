"""
Accepted
725 [Hard]
Runtime: 44 ms, faster than 19.67% of Python3 online submissions for Split Linked List in Parts.
Memory Usage:  16.91 MB, less than 22.72% of Python3 online submissions for Split Linked List in Parts.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [head for _ in range(k)]

        res = []

        totalNodes = 0
        ptr = head
        while ptr:
            totalNodes += 1
            ptr = ptr.next
        
        extraParts = totalNodes % k

        ptr = head
        for i in range(k):
            head = ptr
            if extraParts:
                curPartSize = (totalNodes // k) + 1
                extraParts -= 1
            else:
                curPartSize = totalNodes // k

            for j in range(curPartSize - 1):
                if ptr:
                    ptr = ptr.next

            if ptr:
                nextPartHead = ptr.next
                ptr.next = None
                ptr = nextPartHead

            res.append(head)

        return res