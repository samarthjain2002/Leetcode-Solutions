"""
Accepted
3577 [Medium]
Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Count the Number of Computer Unlocking Permutations.
Memory Usage: 32.11 MB, less than 100.00% of Python3 online submissions for Count the Number of Computer Unlocking Permutations.
"""
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
                
        MOD = 10**9 + 7
        res = 1
        for i in range(1, len(complexity)):
            res *= i
            res %= MOD
        return res