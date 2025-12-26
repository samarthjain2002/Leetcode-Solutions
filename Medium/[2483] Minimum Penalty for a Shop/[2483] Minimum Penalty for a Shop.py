"""
Accepted
2483 [Medium]
Runtime: 47 ms, faster than 80.77% of Python3 online submissions for Minimum Penalty for a Shop.
Memory Usage: 17.85 MB, less than 98.14% of Python3 online submissions for Minimum Penalty for a Shop.
"""
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minPen = customers.count('N')
        curPen = minPen
        res = len(customers)
        for i in reversed(range(len(customers))):
            if customers[i] == 'Y':
                curPen += 1
            else:
                curPen -= 1
            
            if curPen <= minPen:
                res = i
                minPen = curPen
        return res