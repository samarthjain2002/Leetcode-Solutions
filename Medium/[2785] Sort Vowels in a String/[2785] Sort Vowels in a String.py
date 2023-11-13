"""
Accepted
2785 [Medium]
Runtime: 264 ms, faster than 20.50% of Python3 online submissions for Sort Vowels in a String.
Memory Usage: 18.86 MB, less than 80.37% of Python3 online submissions for Sort Vowels in a String.
"""
class Solution:
    def sortVowels(self, s: str) -> str:
        
        list1 = []
        t = ""
        count = 0
        
        for i in range(0,len(s)):
            if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' or s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                list1.append(s[i])

        list1.sort()

        for i in range(0,len(s)):
            if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' or s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                t += list1[count]
                count += 1
            else:
                t += s[i]

        return t