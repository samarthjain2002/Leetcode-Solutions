"""
Accepted
2342 [Easy]
Runtime: 386 ms, faster than 45.62% of Python3 online submissions for Max Sum of a Pair With Equal Sum of Digits.
Memory Usage: 33.66 MB, less than 52.32% of Python3 online submissions for Max Sum of a Pair With Equal Sum of Digits.
"""
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        pairs = {}

        for num in nums:
            s = 0
            for dig in str(num):
                s += int(dig)

            if s not in pairs:
                pairs[s] = [-float("inf"), -float("inf")]

            if num > pairs[s][0]:
                pairs[s][1] = pairs[s][0]
                pairs[s][0] = num
            elif num > pairs[s][1]:
                pairs[s][1] = num
                
        res = -1
        for key, pair in pairs.items():
            if pair[0] > -float("inf") and pair[1] > -float("inf"):
                res = max(res, pair[0] + pair[1])
        return res