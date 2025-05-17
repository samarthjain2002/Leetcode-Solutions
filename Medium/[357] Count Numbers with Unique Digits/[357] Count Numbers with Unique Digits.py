"""
Accepted
357 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Count Numbers with Unique Digits.
Memory Usage: 17.93 MB, less than 12.25% of Python3 online submissions for Count Numbers with Unique Digits.
"""
# Math solution (Kinda like Dynamic Programming)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        res = 10
        for digitSize in range(2, n + 1):
            digits_available = 9
            total = 1
            for _ in range(digitSize - 1):
                total = total * digits_available
                digits_available -= 1
            total = total * 9
            res += total
        return res



"""
Runtime: 3544 ms, faster than 5.07% of Python3 online submissions for Count Numbers with Unique Digits.
Memory Usage: 17.92 MB, less than 12.25% of Python3 online submissions for Count Numbers with Unique Digits.
"""
# Bakctracking approach
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        res = 0
        hashSet = set()
        def backtrack(num):
            nonlocal res
            if len(num) > n:
                return

            res += 1
            for i in range(10):
                if len(num) == 0 and i == 0:
                    continue
                if i not in hashSet:
                    hashSet.add(i)
                    backtrack(num + str(i))
                    hashSet.remove(i)


        backtrack("")
        return res