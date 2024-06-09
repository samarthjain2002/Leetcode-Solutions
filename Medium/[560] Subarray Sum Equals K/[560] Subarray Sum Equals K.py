"""
Accepted
560 [Medium]
Runtime: 221 ms, faster than 61.27% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage:  19.32 MB, less than 91.05% of Python3 online submissions for Subarray Sum Equals K.
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        hashMap = {0: 1}
        res = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in hashMap:
                res += hashMap[prefixSum - k]
            if prefixSum in hashMap:
                hashMap[prefixSum] += 1
            else:
                hashMap[prefixSum] = 1
        return res