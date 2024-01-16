"""
Accepted
151 [Medium]
Runtime: 53 ms, faster than 13.34% of Python3 online submissions for Reverse Words in a String.
Memory Usage:  17.40 MB, less than 41.38% of Python3 online submissions for Reverse Words in a String.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        left, right = 0, 0
        while right <= len(s):
            if right == len(s) or s[right] == ' ':
                if s[left: right]:
                    words.append(s[left: right])
                right += 1
                left = right
            else:
                right += 1
        
        revString = ""
        for i in range(len(words) - 1, -1, -1):
            revString += words[i] + ' '

        return revString[:-1]