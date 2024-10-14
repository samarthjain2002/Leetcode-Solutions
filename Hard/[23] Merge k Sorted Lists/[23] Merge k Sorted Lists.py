"""
Accepted
23 [Hard]
Runtime: 65 ms, faster than 96.70% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage:  19.90 MB, less than 41.57% of Python3 online submissions for Merge k Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None

        minHeap = []
        for i in range(k):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        
        if minHeap:
            val, i, location = heapq.heappop(minHeap)
            res = ListNode(val)
            if location.next:
                heapq.heappush(minHeap, (location.next.val, i, location.next))
            ptr = res
        else:
            return None

        while minHeap:
            val, i, location = heapq.heappop(minHeap)
            newNode = ListNode(val)
            ptr.next = newNode
            ptr = ptr.next

            if location.next:
                heapq.heappush(minHeap, (location.next.val, i, location.next))

        return res