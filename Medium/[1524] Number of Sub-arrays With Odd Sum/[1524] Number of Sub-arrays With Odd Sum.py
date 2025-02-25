"""
Accepted
1524 [Medium]
Runtime: 74 ms, faster than 65.32% of Python online submissions for Number of Sub-arrays With Odd Sum.
Memory Usage: 21.87 MB, less than 66.67% of Python online submissions for Number of Sub-arrays With Odd Sum.
"""
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = 0
        odd_cnt = even_cnt = 0
        res = 0

        for num in arr:
            cur_sum += num
            if cur_sum % 2:
                res += 1 + even_cnt
                odd_cnt += 1
            else:
                res += odd_cnt
                even_cnt += 1
            res = res % (10**9 + 7)
        return res