"""
Accepted
3848 [Medium]
Runtime: 6 ms, faster than 46.29% of Python3 online submissions for Check Digitorial Permutation.
Memory Usage: 19.30 MB less than 96.64% of Python3 online submissions for Check Digitorial Permutation.
"""
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        fact = {0: 1}
        num = 1
        for i in range(1, 10):
            num *= i
            fact[i] = num

        s = 0
        for dig in str(n):
            s += fact[int(dig)]

        arr1 = [0] * 10
        arr2 = [0] * 10
        for dig in str(n):
            arr1[int(dig)] += 1
        for dig in str(s):
            arr2[int(dig)] += 1
        
        return arr1 == arr2