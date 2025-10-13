"""
Accepted
2273 [Easy]
Runtime: 11 ms, faster than 33.70% of Python3 online submissions for Find Resultant Array After Removing Anagrams.
Memory Usage: 17.76 MB, less than 76.67% of Python3 online submissions for Find Resultant Array After Removing Anagrams.
"""
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def checkAnagram(word1, word2):
            freq1, freq2 = [0] * 26, [0] * 26
            for char in word1:
                freq1[ord(char) - ord('a')] += 1
            for char in word2:
                freq2[ord(char) - ord('a')] += 1
            return freq1 == freq2

        stack = []
        for word in words:
            if stack:
                if checkAnagram(stack[-1], word):
                    pass
                else:
                    stack.append(word)
            else:
                stack.append(word)
        return stack