"""
Accepted
611 [Medium]
Runtime: 5068 ms, faster than 5.05% of Python3 online submissions for Valid Triangle Number.
Memory Usage: 17.60 MB, less than 96.03% of Python3 online submissions for Valid Triangle Number.
"""
# Sorting + Binary Search solution
# TC: O(n^2(log(n))), SC: O(n) for sorting
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                k = -1
                low, high = j + 1, len(nums) - 1
                while low <= high:
                    mid = low + ((high - low) // 2)
                    if nums[i] + nums[j] > nums[mid]:
                        k = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                
                if k > j:
                    res += k - j

        return res



# TLE
# Sorting solution
# TC: O(n^3), SC: o(n)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] > nums[k]:
                        res += 1
                    else:
                        break

        return res