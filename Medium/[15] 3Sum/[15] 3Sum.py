"""
Accepted
15 [Medium]
Runtime: 737 ms, faster than 58.07% of Python3 online submissions for 3Sum.
Memory Usage: 20.66 MB, less than 77.98% of Python3 online submissions for 3Sum.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        N = len(nums)
        for i in range(N - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, N - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return res