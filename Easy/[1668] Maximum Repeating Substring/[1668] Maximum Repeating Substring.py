"""
Accepted
2302 [Easy]
Runtime: 4 ms, faster than 5.19% of Python3 online submissions for Count Subarrays With Score Less Than K.
Memory Usage: 17.90 MB, less than 11.64% of Python3 online submissions for Count Subarrays With Score Less Than K.
"""
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        M, N = len(sequence), len(word)
        cache = {}

        def dfs(index):
            if index in cache:
                return cache[index]
            if index == len(sequence):
                return 0

            for i in range(N):
                if index + i == M or sequence[index + i] != word[i]:
                    cache[index] = 0
                    return 0
            
            cache[index] = 1 + dfs(index + len(word))
            return cache[index]


        res = 0
        for i in range(M):
            res = max(res, dfs(i))
        return res