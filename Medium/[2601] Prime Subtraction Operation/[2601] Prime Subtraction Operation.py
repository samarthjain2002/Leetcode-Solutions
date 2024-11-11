"""
Accepted
2601 [Medium]
Runtime: 1061 ms, faster than 5.03% of Python3 online submissions for Prime Subtraction Operation.
Memory Usage: 16.87 MB, less than 35.50% of Python3 online submissions for Prime Subtraction Operation.
"""
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        N = len(nums)

        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        def findPrime(y, x):
            for p in range(y - 1, 1, -1):
                if isPrime(p) and y - p > x:
                    return p
            return 0

        for i in range(N):
            if i == 0:
                p = findPrime(nums[i], 0)
            else:
                p = findPrime(nums[i], nums[i - 1])
                
            if p:
                nums[i] = nums[i] - p
            elif i > 0 and nums[i] <= nums[i - 1]:
                return False
        return True