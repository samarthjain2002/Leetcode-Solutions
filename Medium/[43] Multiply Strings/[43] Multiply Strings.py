"""
Accepted
43 [Medium]
Runtime: 110 ms, faster than 14.66% of Python3 online submissions for Multiply Strings.
Memory Usage: 16.66 MB, less than 20.15% of Python3 online submissions for Multiply Strings.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            left = num2
            right = num1
        else:
            left = num1
            right = num2

        pointer = -1
        starter = -1
        lis = [0] * 400
        for r in reversed(right):
            for l in reversed(left):
                mul = int(r) * int(l)
                if mul > 9:
                    lis[pointer] += mul % 10
                    mul = mul // 10
                    pointer -= 1
                    lis[pointer] += mul
                else:
                    lis[pointer] += mul
                    pointer -= 1
            starter -= 1
            pointer = starter

        for i in range(399, -1, -1):
            if lis[i] > 9:
                temp = lis[i]
                lis[i] = temp % 10
                temp = temp // 10
                lis[i - 1] += temp

        res = 0
        m = 1
        for i in range(399, -1, -1):
            res += lis[i] * m
            m *= 10
        return str(res)