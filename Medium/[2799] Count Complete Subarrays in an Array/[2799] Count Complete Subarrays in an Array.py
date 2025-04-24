"""
Accepted
2799 [Medium]
Runtime: 7 ms, faster than 95.10% of Python3 online submissions for Count Complete Subarrays in an Array.
Memory Usage: 18.06 MB, less than 46.50% of Python3 online submissions for Count Complete Subarrays in an Array.
"""
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))

        numFreq = defaultdict(int)
        numCount = 0
        left = 0
        res = 0
        for right in range(len(nums)):
            numFreq[nums[right]] += 1
            if numFreq[nums[right]] == 1:
                numCount += 1

            while numCount == distinct:
                res += len(nums) - right
                numFreq[nums[left]] -= 1
                if numFreq[nums[left]] == 0:
                    numCount -= 1
                left += 1
                
        return res