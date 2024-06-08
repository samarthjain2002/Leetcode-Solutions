"""
Accepted
523 [Medium]
Runtime: 1166 ms, faster than 5.02% of Python3 online submissions for Continuous Subarray Sum.
Memory Usage:  36.36 MB, less than 36.90% of Python3 online submissions for Continuous Subarray Sum.
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
            return False

        remainderMap = {0: -1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            remainder = sum % k
            if remainder < 0:
                remainder += k

            if remainder in remainderMap:
                prevIndex = remainderMap[remainder]
                if i - prevIndex > 1:
                    return True
            else:
                remainderMap[remainder] = i
        return False