"""
Accepted
2364 [Medium]
Runtime: 587 ms, faster than 53.03% of Python3 online submissions for Count Number of Bad Pairs.
Memory Usage: 34.77MB, less than 93.18% of Python3 online submissions for Count Number of Bad Pairs.
"""
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            nums[i] = nums[i] - i

        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        count = 0
        for i in d:
            if d[i] == 2:
                count += 1
            if d[i] > 2:
                count += int(((d[i] * (d[i] + 1)) / 2) - d[i])

        count = int(((len(nums) * (len(nums) + 1)) / 2) - len(nums)) - count

        return count