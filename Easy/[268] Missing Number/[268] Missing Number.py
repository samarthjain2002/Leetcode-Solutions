"""
Accepted
268 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Missing Number.
Memory Usage: 18.59 MB, less than 92.16% of Python3 online submissions for Missing Number.
"""
# Math approach
# TC: O(1), SC: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        req_sum = (len(nums) * (len(nums) + 1)) // 2
        actual_sum = sum(nums)
        return req_sum - actual_sum



"""
Runtime: 3 ms, faster than 63.88% of Python3 online submissions for Missing Number.
Memory Usage: 18.60 MB, less than 92.16% of Python3 online submissions for Missing Number.
"""
# Bit Manipulation/XOR approach
# TC: O(n), SC: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums) + 1):
            xor = xor ^ i

        for num in nums:
            xor = xor ^ num

        return xor



"""
Runtime: 12 ms, faster than 21.47% of Python3 online submissions for Missing Number.
Memory Usage: 18.76 MB, less than 52.15% of Python3 online submissions for Missing Number.
"""
# Binary Search approach
# TC: O(nlog(n)), SC: (1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        low, high = 0, len(nums) 
        while low < high:
            mid = low + ((high - low) // 2)

            # nums[mid] can either be equal or greater than mid, never lesser
            if nums[mid] != mid:
                high = mid
            else:
                low = mid + 1

        # Here, low = high
        return low



"""
Runtime: 1303 ms, faster than 7.07% of Python3 online submissions for Missing Number.
Memory Usage: 18.64 MB, less than 72.61% of Python3 online submissions for Missing Number.
"""
# Brute-force approach
# TC: O(n^2), SC: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
