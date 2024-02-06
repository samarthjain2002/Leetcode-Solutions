"""
Accepted
1 [Easy]
Runtime: 48 ms, faster than 98.08% of Python3 online submissions for Two Sum.
Memory Usage: 17.78 MB, less than 66.28% of Python3 online submissions for Two Sum.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        N = len(nums)
        for i in range(N):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            else:
                hashMap[nums[i]] = i