"""
Accepted
1657 [Medium]
Runtime: 197 ms, faster than 43.00% of Python3 online submissions for Determine if Two Strings Are Close.
Memory Usage: 18.28 MB, less than 38.39% of Python3 online submissions for Determine if Two Strings Are Close.
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        w1Dict = defaultdict(int)
        w2Dict = defaultdict(int)
        for i in range(len(word1)):
            w1Dict[word1[i]] += 1
            w2Dict[word2[i]] += 1
            
        w1count, w2count = [], []
        for key, value in w1Dict.items():
            if key not in w2Dict:
                return False
            w1count.append(value)
        for key, value in w2Dict.items():
            if key not in w1Dict:
                return False
            w2count.append(value)

        w1count.sort()
        w2count.sort()

        if w1count == w2count:
            return True
        else:
            return False