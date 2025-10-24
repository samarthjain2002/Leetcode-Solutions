"""
Accepted
2048 [Medium]
Runtime: 4122 ms, faster than 21.51% of Python3 online submissions for Next Greater Numerically Balanced Number.
Memory Usage: 17.70 MB, less than 65.53% of Python3 online submissions for Next Greater Numerically Balanced Number.
"""
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        num = n + 1
        while True:
            freq = Counter(str(num))
            for dig, fr in freq.items():
                if int(dig) != fr:
                    break
            else:
                return num
            num += 1