"""
Accepted
974 [Medium]
Runtime: 230 ms, faster than 56.97% of Python3 online submissions for Subarray Sums Divisible by K.
Memory Usage:  21.38 MB, less than 87.31% of Python3 online submissions for Subarray Sums Divisible by K.
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        hashMap = {0: 1}    #Key is remainder and Value is count
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum % k in hashMap:
                res += hashMap[sum % k]
                hashMap[sum % k] += 1
            else:
                hashMap[sum % k] = 1
        return res