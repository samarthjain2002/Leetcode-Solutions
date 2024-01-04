"""
Accepted
2870 [Medium]
Runtime: 556 ms, faster than 99.70% of Python3 online submissions for Minimum Number of Operations to Make Array Empty.
Memory Usage: 32.38 MB, less than 6.06% of Python3 online submissions for Minimum Number of Operations to Make Array Empty.
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for c in count.values():
            if c == 1:
                return -1
            res += math.ceil(c / 3)
        return res