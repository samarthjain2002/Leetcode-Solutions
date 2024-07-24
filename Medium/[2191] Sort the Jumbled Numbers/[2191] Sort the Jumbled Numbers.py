"""
Accepted
2191 [Medium]
Runtime: 1206 ms, faster than 23.91% of Python3 online submissions for Sort the Jumbled Numbers.
Memory Usage: 25.56 MB, less than 33.70% of Python3 online submissions for Sort the Jumbled Numbers.
"""
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i, num in enumerate(nums):
            s = ""
            for digit in str(num):
                s += str(mapping[int(digit)])
            pairs.append([int(s), i])

        pairs.sort()
        
        return [nums[b] for a, b in pairs]