"""
Accepted
1897 [Easy]
Runtime: 55 ms, faster than 81.90% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
Memory Usage: 17.45 MB, less than 9.52% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
"""
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True

        letterDict = {}
        for word in words:
            for letter in word:
                if letter not in letterDict:
                    letterDict[letter] = 1
                else:
                    letterDict[letter] += 1

        for value in letterDict.values():
            if value % len(words) != 0:
                return False

        return True