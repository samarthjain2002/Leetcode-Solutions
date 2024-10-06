"""
Accepted
1813 [Medium]
Runtime: 30 ms, faster than 86.96% of Python3 online submissions for Sentence Similarity III.
Memory Usage: 16.70 MB, less than 13.04% of Python3 online submissions for Sentence Similarity III.
"""
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sen1 = sentence1.split(' ')
        sen2 = sentence2.split(' ')

        longestPrefix, shortestPrefix = 0, 0
        for i in range(min(len(sen1), len(sen2))):
            if sen1[i] == sen2[i]:
                longestPrefix += 1
            else:
                break
                
        for i in range(min(len(sen1), len(sen2))):
            if sen1[-1 - i] == sen2[-1 - i]:
                shortestPrefix += 1
            else:
                break
                
        if len(sen1) - longestPrefix - shortestPrefix <= 0:
            return True
        elif len(sen2) - longestPrefix - shortestPrefix <= 0:
            return True
        else:
            return False