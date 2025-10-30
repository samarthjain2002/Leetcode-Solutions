"""
Accepted
1526 [Hard]
Runtime: 24 ms, faster than 83.07% of Python3 online submissions for Minimum Number of Increments on Subarrays to Form a Target Array.
Memory Usage: 26.59 MB, less than 96.16% of Python3 online submissions for Minimum Number of Increments on Subarrays to Form a Target Array.
"""
# TC: O(n), SC: O(1)
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        res = 0
        for num in target:
            if num > prev:
                res += num - prev
            prev = num
        return res