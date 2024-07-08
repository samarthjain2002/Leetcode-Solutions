"""
Accepted
1814 [Medium]
Runtime: 649 ms, faster than 27.19% of Python3 online submissions for Count Nice Pairs in an Array.
Memory Usage: 26.84 MB, less than 33.99% of Python3 online submissions for Count Nice Pairs in an Array.
"""
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        revNums = []
        for i in nums:
            revNums.append(i - int(''.join(reversed(str(i)))))

        d = {}
        for i in revNums:
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

        return count % 1000000007