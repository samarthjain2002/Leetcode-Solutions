"""
Accepted
167 [Medium]
Runtime: 108 ms, faster than 72.88% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage:  17.45 MB, less than 60.00% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1