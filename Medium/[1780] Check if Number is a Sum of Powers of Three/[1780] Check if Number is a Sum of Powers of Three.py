"""
Accepted
1780 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
Memory Usage: 17.74 MB, less than 59.96% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
"""
# Math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        exp = 0
        while 3**(exp + 1) <= n:
            exp += 1

        while exp >= 0:
            power = 3**exp
            if power <= n:
                n -= power
            if power <= n:
                return False

            exp -= 1

        return n == 0



"""
Runtime: 266 ms, faster than 5.58% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
Memory Usage: 17.88 MB, less than 38.84% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
"""
# Backtracking
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        def backtrack(exp, curSum):
            if curSum == n:
                return True
            if curSum > n or 3**exp > n:
                return False

            if backtrack(exp + 1, curSum + 3**exp):
                return True
            return backtrack(exp + 1, curSum)

        return backtrack(0, 0)



"""
Runtime: 999 ms, faster than 5.58% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
Memory Usage: 18.00 MB, less than 18.33% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
"""
# Recursion
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr = []
        for exp in range(16):
            arr.append(3**exp)
            
        
        def rec(i, curSum):
            if i == len(arr):
                return False
            if curSum == n:
                return True

            return rec(i + 1, curSum + arr[i]) or rec(i + 1, curSum)

        return rec(0, 0)