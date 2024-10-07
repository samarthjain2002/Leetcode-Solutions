"""
Accepted
160 [Easy]
Runtime: 77 ms, faster than 75.69% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 27.28 MB, less than 30.73% of Python3 online submissions for Intersection of Two Linked Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aLen, bLen = 0, 0
        ptr = headA
        while ptr != None:
            aLen += 1
            ptr = ptr.next
        ptr = headB
        while ptr != None:
            bLen += 1
            ptr = ptr.next
            
        if aLen > bLen:
            ptr = headA
            i = aLen - bLen
            while ptr and i != 0:
                ptr = ptr.next
                i -= 1
            ptrA = ptr
            ptrB = headB
        elif bLen > aLen:
            ptr = headB
            i = bLen - aLen
            while ptr and i != 0:
                ptr = ptr.next
                i -= 1
            ptrB = ptr
            ptrA = headA
        else:
            ptrA = headA
            ptrB = headB
            
        while ptrA:
            if ptrA == ptrB:
                return ptrA
            else:
                ptrA = ptrA.next
                ptrB = ptrB.next
        return None