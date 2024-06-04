"""
Accepted
13 [Easy]
Runtime: 37 ms, faster than 93.12% of Python3 online submissions for Roman to Integer.
Memory Usage: 16.48 MB, less than 94.25% of Python3 online submissions for Roman to Integer.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        N = len(s)
        hashMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(N - 1, -1, -1):
            res += hashMap[s[i]]
            if i > 0:
                if s[i - 1] == 'I' and (s[i] == 'V' or s[i] == 'X'):
                    res -= hashMap['I'] * 2
                elif s[i - 1] == 'X' and (s[i] == 'L' or s[i] == 'C'):
                    res -= hashMap['X'] * 2
                elif s[i - 1] == 'C' and (s[i] == 'D' or s[i] == 'M'):
                    res -= hashMap['C'] * 2
        return res