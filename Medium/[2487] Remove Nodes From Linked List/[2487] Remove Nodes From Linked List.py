"""
Accepted
2487 [Medium]
Runtime: 525 ms, faster than 21.06% of Python3 online submissions for Remove Nodes From Linked List.
Memory Usage: 60.42 MB, less than 29.38% of Python3 online submissions for Remove Nodes From Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        ptr = head
        while ptr != None:
            lis.append(ptr.val)
            ptr = ptr.next

        count = lis[-1]
        newLis = [lis[-1]]
        for i in lis[-2::-1]:
            if i >= count:
                newLis.append(i)
                count = i

        head = ListNode(newLis[-1])
        ptr = head
        for i in newLis[-2::-1]:
            head.next = ListNode(i)
            head = head.next

        return ptr