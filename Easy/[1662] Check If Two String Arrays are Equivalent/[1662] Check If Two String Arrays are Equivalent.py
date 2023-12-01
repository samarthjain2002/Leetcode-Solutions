"""
Accepted
1662 [Easy]
Runtime: 51 ms, faster than 5.43% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 16.39 MB, less than 28.02% of Python3 online submissions for Check If Two String Arrays are Equivalent
"""
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1of2 = ""
        for i in word1:
            word1of2 += i

        word2of2 = ""
        for j in word2:
            word2of2 += j

        if word1of2 == word2of2:
            return True
        else:
            return False