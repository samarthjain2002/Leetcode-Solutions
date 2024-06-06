"""
Accepted
219 [Easy]
Runtime: 442 ms, faster than 94.95% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 29.70 MB, less than 64.68% of Python3 online submissions for Contains Duplicate II.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i, n in enumerate(nums):
            if n in d and abs(i - d[n]) <= k:
                return True
            else:
                d[n] = i
        
        return False