"""
Accepted
3349 [Easy]
Runtime: 80 ms, faster than 75.40% of Python3 online submissions for Adjacent Increasing Subarrays Detection I.
Memory Usage: 17.86 MB, less than 45.99% of Python3 online submissions for Adjacent Increasing Subarrays Detection I.
"""
# Sliding Window solution
# TC: O(n), SC: O(1)
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1 and len(nums) > 1:
            return True

        left = 0
        foundOne = False
        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:
                if right - left >= 2 * k:
                    return True
                elif right - left >= k:
                    if foundOne:
                        return True
                    else:
                        foundOne = True
                else:
                    foundOne = False
                left = right

        if nums[-1] > nums[-2]:
            if len(nums) - left >= 2 * k:
                return True
            elif len(nums) - left >= k and foundOne:
                return True
        return False



"""
Runtime: 90 ms, faster than 31.55% of Python3 online submissions for Adjacent Increasing Subarrays Detection I.
Memory Usage: 17.54 MB, less than 98.40% of Python3 online submissions for Adjacent Increasing Subarrays Detection I.
"""
# HashMap solution
# TC: O(n), SC: O(n)
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1 and len(nums) > 1:
            return True
            
        hashMap = {}
        left = 0
        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:
                if right - left >= k:
                    hashMap[left] = right - 1
                left = right
        if nums[-1] > nums[-2] and len(nums) - left >= k:
            hashMap[left] = len(nums) - 1

        for left, right in hashMap.items():
            if right - left + 1 >= 2 * k:
                return True
            elif right + 1 in hashMap:
                return True
        return False