"""
Accepted
632 [Hard]
Runtime: 208 ms, faster than 25.42% of Python3 online submissions for Smallest Range Covering Elements from K Lists.
Memory Usage: 23.00 MB, less than 94.02% of Python3 online submissions for Smallest Range Covering Elements from K Lists.
"""
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        minHeap = []
        
        minValue = maxValue = nums[0][0]
        for listNumber in range(k):
            minValue = min(minValue, nums[listNumber][0])
            maxValue = max(maxValue, nums[listNumber][0])
            heapq.heappush(minHeap, [nums[listNumber][0], listNumber, 0])

        res = [minValue, maxValue]

        while True:
            val, listNumber, index = heapq.heappop(minHeap)

            if index == len(nums[listNumber]) - 1:
                return res

            index += 1
            heapq.heappush(minHeap, [nums[listNumber][index], listNumber, index])

            nextVal = nums[listNumber][index]
            minValue = minHeap[0][0]
            maxValue = max(maxValue, nextVal)
            if res[1] - res[0] > maxValue - minValue:
                res[0], res[1] = minValue, maxValue