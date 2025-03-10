"""
Accepted
3306 [Medium]
Runtime: 6253 ms, faster than 5.21% of Python3 online submissions for Count of Substrings Containing Every Vowel and K Consonants II.
Memory Usage: 18.51 MB, less than 91.33% of Python3 online submissions for Count of Substrings Containing Every Vowel and K Consonants II.
"""
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleast(k):
            N = len(word)

            vowelMap = {vowel: 0 for vowel in "aeiou"}
            cons = 0

            left = 0
            res = 0
            for right in range(N):
                if word[right] in "aeiou":
                    vowelMap[word[right]] += 1
                else:
                    cons += 1

                while all(vowelMap[vowel] for vowel in "aeiou") and cons >= k:
                    res += N - right
                    if word[left] in "aeiou":
                        vowelMap[word[left]] -= 1
                    else:
                        cons -= 1
                    left += 1
                
            return res
            

        return atleast(k) - atleast(k + 1)