"""
Accepted
3005 [Easy]
Runtime: 42 ms, faster than 69.11% of Python3 online submissions for Count Elements With Maximum Frequency.
Memory Usage: 16.49 MB, less than 97.32% of Python3 online submissions for Count Elements With Maximum Frequency.
"""
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for i in nums:
            dict[i] += 1
        
        maximum = 0
        for val in dict.values():
            maximum = max(maximum, val)

        count = 0
        for val in dict.values():
            if val == maximum:
                count += 1

        return count * maximum