"""
Accepted
315 [Hard]
Runtime: 660 ms, faster than 86.79% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 35.62 MB, less than 64.10% of Python3 online submissions for Count of Smaller Numbers After Self.
"""
# SortedList
from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        res = []

        for num in reversed(nums):
            index = SortedList.bisect_left(sl, num)
            res.append(index)
            sl.add(num)
            
        return res[::-1]



"""
Runtime: 660 ms, faster than 86.79% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 35.62 MB, less than 64.10% of Python3 online submissions for Count of Smaller Numbers After Self.
"""
# bisect
import bisect


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        print(len(nums))
        sortedList = []
        res = []
        for num in reversed(nums):
            index = bisect.bisect_left(sortedList, num)
            res.append(index)
            bisect.insort_left(sortedList, num)
            
        return res[::-1]