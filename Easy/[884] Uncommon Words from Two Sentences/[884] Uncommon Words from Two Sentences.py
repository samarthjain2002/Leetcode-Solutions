"""
Accepted
884 [Easy]
Runtime: 37 ms, faster than 44.90% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 16.63 MB, less than 5.76% of Python3 online submissions for Uncommon Words from Two Sentences.
"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ls1 = s1.split(' ')
        ls2 = s2.split(' ')

        res = []
        for word in ls1:
            if ls1.count(word) == 1 and word not in ls2:
                res.append(word)
        for word in ls2:
            if ls2.count(word) == 1 and word not in ls1:
                res.append(word)
        return res