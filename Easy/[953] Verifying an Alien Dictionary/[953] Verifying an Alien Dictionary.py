"""
Accepted
953 [Easy]
Runtime: 6 ms, faster than 16.78% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 17.74 MB, less than 74.95% of Python3 online submissions for Verifying an Alien Dictionary.
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {char: idx for idx, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False

                if word1[j] != word2[j]:
                    if orderDict[word1[j]] > orderDict[word2[j]]:
                        return False
                    break
        return True