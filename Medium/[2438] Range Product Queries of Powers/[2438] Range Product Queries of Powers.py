"""
Accepted
2438 [Medium]
Runtime: 50 ms, faster than 75.16% of Python3 online submissions for Range Product Queries of Powers.
Memory Usage: 48.31 MB, less than 5.59% of Python3 online submissions for Range Product Queries of Powers.
"""
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        powers = []
        for i, bit in enumerate(reversed(bin(n)[2 : ])):
            if bit == '1':
                powers.append(2**i)

        prefix = [powers[0]]
        for i in range(1, len(powers)):
            prefix.append(powers[i] * prefix[i - 1])

        answers = []
        for left, right in queries:
            if left > 0:
                answers.append((prefix[right] // prefix[left - 1]) % MOD)
            else:
                answers.append(prefix[right] % MOD)

        return answers



"""
Runtime: 263 ms, faster than 9.94% of Python3 online submissions for Range Product Queries of Powers.
Memory Usage: 48.30 MB, less than 17.39% of Python3 online submissions for Range Product Queries of Powers.
"""
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        powers = []
        for i, bit in enumerate(reversed(bin(n)[2 : ])):
            if bit == '1':
                powers.append(2**i)

        answers = []
        for left, right in queries:
            res = 1
            for i in range(left, right + 1):
                res *= powers[i]
                res %= MOD
            
            answers.append(res)

        return answers