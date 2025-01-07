"""
Accepted
72 [Medium]
Runtime: 49 ms, faster than 80.14% of Python3 online submissions for Edit Distance.
Memory Usage: 19.46 MB, less than 76.08% of Python3 online submissions for Edit Distance.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def rec(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j

            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                dp[(i, j)] = rec(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(rec(i, j + 1), rec(i + 1, j), rec(i + 1, j + 1))
            return dp[(i, j)]

        return rec(0, 0)