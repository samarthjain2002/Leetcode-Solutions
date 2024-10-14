"""
Accepted
2208 [Medium]
Runtime: 785 ms, faster than 58.44% of Python3 online submissions for Minimum Operations to Halve Array Sum.
Memory Usage: 31.27 MB, less than 91.77% of Python3 online submissions for Minimum Operations to Halve Array Sum.
"""
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        N = len(nums)
        half = sum(nums) / 2
        nums = [-num for num in nums]
        heapq.heapify(nums)

        count, res = 0, 0
        for i in range(N):
            pop = -1 * heapq.heappop(nums)
            res += 1

            count += pop / 2
            if count >= half:
                return res

            heapq.heappush(nums, -1 * pop / 2)