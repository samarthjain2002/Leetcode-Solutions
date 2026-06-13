"""
Accepted
3838 [Easy]
Runtime: 8 ms, faster than 64.03% of Python3 online submissions for Weighted Word Mapping.
Memory Usage: 19.31 MB, less than 33.64% of Python3 online submissions for Weighted Word Mapping.
"""
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            weight = 0
            for char in word:
                weight += weights[ord(char) - ord('a')]
            m = 25 - (weight % 26)
            res.append(chr(ord('a') + m))
        return "".join(res)