"""
Accepted
3403 [Medium]
Runtime: 2548 ms, faster than 9.85% of Python3 online submissions for Find the Lexicographically Largest String From the Box I.
Memory Usage: 18.11 MB, less than 18.94% of Python3 online submissions for Find the Lexicographically Largest String From the Box I.
"""
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
            
        maxLength = len(word) - numFriends + 1

        res = word[ : maxLength]
        for i in range(1, len(word)):
            for j in range(min(len(word) - i, maxLength)):
                if ord(word[i + j]) > ord(res[j]):
                    res = word[i : i + min(len(word) - i, maxLength)]
                    break
                elif ord(word[i + j]) < ord(res[j]):
                    break
                    
        return res