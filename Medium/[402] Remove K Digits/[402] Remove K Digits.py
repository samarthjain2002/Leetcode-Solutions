"""
Accepted
402 [Medium]
Runtime: 68 ms, faster than 29.51% of Python3 online submissions for Remove K Digits.
Memory Usage:  17.98 MB, less than 73.15% of Python3 online submissions for Remove K Digits.
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monotonicStack = []
        N = len(num)
        for i in range(N):
            while monotonicStack and monotonicStack[-1] > num[i] and k > 0:
                monotonicStack.pop()
                k -= 1
            monotonicStack.append(num[i])
        while k != 0:
            monotonicStack.pop()
            k -= 1

        res = ""
        N = len(monotonicStack)
        for i in monotonicStack:
            res += i

        if res == "":
            return "0"
        else:
            N = len(res)
            for i in range(N):
                if res[i] != '0':
                    return res[i : ]
            return "0"