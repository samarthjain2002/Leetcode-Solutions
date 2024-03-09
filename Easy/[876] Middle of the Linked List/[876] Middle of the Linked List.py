"""
Accepted
876 [Easy]
Runtime: 45 ms, faster than 7.35% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 16.58 MB, less than 36.63% of Python3 online submissions for Middle of the Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        flag = False
        while head != None:
            if flag:
                ptr = ptr.next
                flag = False
            else:
                flag = True
            head = head.next
            
        return ptr