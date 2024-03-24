"""
Accepted
1768 [Easy]
Runtime: 30 ms, faster than 88.04% of Python3 online submissions for Merge Strings Alternately.
Memory Usage: 16.49 MB, less than 93.82% of Python3 online submissions for Merge Strings Alternately.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N = min(len(word1), len(word2))
        res = ""
        for i in range(N):
            res += word1[i]
            res += word2[i]

        return res + word1[N : ] + word2[N : ]