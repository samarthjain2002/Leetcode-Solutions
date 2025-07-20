"""
Accepted
3136 [Easy]
Runtime: 1 ms, faster than 26.07% of Python3 online submissions for Valid Word.
Memory Usage: 17.90 MB, less than 13.71% of Python3 online submissions for Valid Word.
"""
class Solution:
    def isValid(self, word: str) -> bool:
        vowel = consonant = False
        for char in word:
            if char not in string.ascii_letters + string.digits:
                return False
        
            if char in "aeiouAEIOU":
                vowel = True
            elif char in string.ascii_letters:
                consonant = True
            
        return vowel and consonant and len(word) >= 3