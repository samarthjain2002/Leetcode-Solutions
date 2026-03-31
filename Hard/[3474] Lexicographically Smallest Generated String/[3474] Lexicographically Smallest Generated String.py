"""
Accepted
3474 [Hard]
Runtime: 206 ms, faster than 64.10% of Python3 online submissions for Lexicographically Smallest Generated String.
Memory Usage: 19.43 MB, less than 51.28% of Python3 online submissions for Lexicographically Smallest Generated String.
"""
# TC: O(n * m), SC: O(N)
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        def isSame(i):
            for j in range(m):
                if word[i + j] != str2[j]:
                    return False
            return True

        n = len(str1)
        m = len(str2)
        N = n + m - 1

        word = ['$'] * N
        canChange = [False] * N

        # Process 'T' in str1
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] != '$' and word[i + j] != str2[j]:
                        return ""
                    word[i + j] = str2[j]

        # Mark and fill the word
        for i in range(N):
            if word[i] == '$':
                word[i] = 'a'
                canChange[i] = True

        # Process 'F' in str1
        for i in range(n):
            if str1[i] == 'F':
                # Check if substring violates inequality
                if isSame(i):
                    for j in range(i + m - 1, i - 1, -1):
                        if canChange[j]:    # Break the equality
                            word[j] = 'b'
                            break
                    else:   # Unable to break equality
                        return ""

        return "".join(word)