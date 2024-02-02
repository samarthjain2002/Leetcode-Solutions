"""
Accepted
1291 [Medium]
Runtime: 41 ms, faster than 28.88% of Python3 online submissions for Sequential Digits.
Memory Usage: 16.48 MB, less than 72.98% of Python3 online submissions for Sequential Digits.
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        M, N = len(str(low)), len(str(high))

        for i in range(M, N + 1):
            for j in range(0, 9 - i + 1):
                sub_string = s[j : j + i]
                sub_string_int = int(sub_string)
                if low <= sub_string_int <= high:
                    res.append(sub_string_int)

        res.sort()

        return res