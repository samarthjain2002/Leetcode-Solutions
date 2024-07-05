"""
Accepted
2058 [Medium]
Runtime: 336 ms, faster than 84.79% of Python3 online submissions for Find the Minimum and Maximum Number of Nodes Between Critical Points.
Memory Usage: 44.65 MB, less than 7.98% of Python3 online submissions for Find the Minimum and Maximum Number of Nodes Between Critical Points.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next.next:
            prev, cur, nex = head, head.next, head.next.next
        else:
            return [-1,-1]

        criticalPoints = []
        count = 1
        while nex:
            count += 1
            if (cur.val > prev.val and cur.val > nex.val) or (cur.val < prev.val and cur.val < nex.val):
                criticalPoints.append(count)
            prev, cur, nex = prev.next, cur.next, nex.next
            
        
        if len(criticalPoints) <= 1:
            return [-1, -1]
            
        minDistance = float("inf")
        for i in range(1, len(criticalPoints)):
            minDistance = min(minDistance, criticalPoints[i] - criticalPoints[i - 1])
        return [minDistance, criticalPoints[-1] - criticalPoints[0]]