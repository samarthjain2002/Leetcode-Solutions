"""
Accepted
1701 [Medium]
Runtime: 767 ms, faster than 27.15% of Python3 online submissions for Average Waiting Time.
Memory Usage: 57.25 MB, less than 9.97% of Python3 online submissions for Average Waiting Time.
"""
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prep = customers[0][0]
        avg = 0
        for ar, ti in customers:
            if prep < ar:
                prep = ar
            prep += ti
            avg += prep - ar
        return avg / len(customers)