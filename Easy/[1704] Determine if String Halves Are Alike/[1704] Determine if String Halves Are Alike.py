"""
Accepted
1704 [Easy]
Runtime: 35 ms, faster than 90.17% of Python3 online submissions for Determine if String Halves Are Alike.
Memory Usage: 17.41 MB, less than 9.07% of Python3 online submissions for Determine if String Halves Are Alike.
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowsInA, vowsInB = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in range(0,int(len(s) / 2)):
            if s[i] in vowels:
                vowsInA += 1
        for i in range(int(len(s) / 2), len(s)):
            if s[i] in vowels:
                vowsInB += 1

        if vowsInA == vowsInB:
            return True
        else:
            return False