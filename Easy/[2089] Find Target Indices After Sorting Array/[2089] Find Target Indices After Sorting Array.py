"""
Accepted
2089 [Easy]
Runtime: 32 ms, faster than 96.94% of Python3 online submissions for Find Target Indices After Sorting Array.
Memory Usage: 16.53 MB, less than 51.83% of Python3 online submissions for Find Target Indices After Sorting Array.
"""
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller_count = target_count = 0
        for num in nums:
            if num < target:
                smaller_count += 1
            elif num == target:
                target_count += 1

        return [i for i in range(smaller_count, smaller_count + target_count)]