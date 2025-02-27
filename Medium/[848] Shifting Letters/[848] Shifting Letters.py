"""
Accepted
848 [Medium]
Runtime: 601 ms, faster than 31.25% of Python3 online submissions for Shifting Letters.
Memory Usage: 30.29 MB, less than 28.92% of Python3 online submissions for Shifting Letters.
"""
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefixSum = sum(shifts)
        res = ""
        for i in range(len(s)):
            temp = prefixSum
            temp = temp % 26
            if ord(s[i]) - ord('a') + temp > 25:
                temp = temp - 26 + ord(s[i]) - ord('a')
                res += chr(ord('a') + temp)
            else:
                res += chr(ord(s[i]) + temp)
            prefixSum -= shifts[i]
        return res