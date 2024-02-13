"""
Accepted
2108 [Easy]
Runtime: 82 ms, faster than 45.08% of Python3 online submissions for Find First Palindromic String in the Array.
Memory Usage: 16.75 MB, less than 59.17% of Python3 online submissions for Find First Palindromic String in the Array.
"""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            wordLen = len(word)
            if wordLen == 1:
                return word
            elif wordLen % 2 == 0:
                right = int(wordLen/2)
            else:
                right = int(wordLen/2) + 1
            left = int(wordLen/2) - 1
            while left > -1 and right < wordLen and word[left] == word[right]:
                if left == 0:
                    return word
                left -= 1
                right += 1

        return ""