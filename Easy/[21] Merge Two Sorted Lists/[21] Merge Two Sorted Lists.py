"""
Accepted
21 [Easy]
Runtime: 42 ms, faster than 10.26% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 16.60 MB, less than 27.42% of Python3 online submissions for Merge Two Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        if list1 and list2:
            if list1.val < list2.val:
                ptr = list1
                cur1 = list1.next
                list2 = None
            else:
                ptr = list2
                cur2 = list2.next
                list1 = None
        elif list1:
            return list1
        else:
            return list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                ptr.next = cur1
                cur1 = cur1.next
                ptr = ptr.next
            else:
                ptr.next = cur2
                cur2 = cur2.next
                ptr = ptr.next
        else:
            if cur1:
                ptr.next = cur1
            else:
                ptr.next = cur2

        if list1:
            return list1
        else:
            return list2



"""
Accepted
21 [Easy]
Runtime: 41 ms, faster than 38.68% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 16.40 MB, less than 96.54% of Python3 online submissions for Merge Two Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive Solution
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2