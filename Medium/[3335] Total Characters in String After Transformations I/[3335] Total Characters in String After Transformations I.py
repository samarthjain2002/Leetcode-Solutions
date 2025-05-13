"""
Accepted
3335 [Medium]
Runtime: 5459 ms, faster than 22.22% of Python3 online submissions for Total Characters in String After Transformations I.
Memory Usage: 18.44 MB, less than 35.29% of Python3 online submissions for Total Characters in String After Transformations I.
"""
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - 97] += 1

        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if freq[i] > 0:
                    if i == 25:
                        new_freq[0] = freq[i]
                        new_freq[1] += freq[i]
                    else:
                        new_freq[i + 1] = freq[i]
            freq = new_freq
        return sum(freq) % (10**9 + 7)