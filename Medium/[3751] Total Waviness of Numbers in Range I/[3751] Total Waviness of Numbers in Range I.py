"""
Accepted
3751 [Medium]
Runtime: 412 ms, faster than 22.22% of Python3 online submissions for Total Waviness of Numbers in Range I.
Memory Usage: 19.24 MB less than 69.73% of Python3 online submissions for Total Waviness of Numbers in Range I.
"""
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for num in range(max(101, num1), num2 + 1):
            n = str(num)
            for i in range(1, len(n) - 1):
                if int(n[i - 1]) < int(n[i]) > int(n[i + 1]):
                    res += 1
                elif int(n[i - 1]) > int(n[i]) < int(n[i + 1]):
                    res += 1
        return res