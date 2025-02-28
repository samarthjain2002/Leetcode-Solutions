"""
Accepted
1092 [Hard]
Runtime: 639 ms, faster than 24.15% of Python3 online submissions for Shortest Common Supersequence.
Memory Usage: 21.70 MB, less than 95.33% of Python3 online submissions for Shortest Common Supersequence.
"""
# TC: O(m * n)
# SC: O(n)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        prev = [str1[j : ] for j in range(len(str1))]
        prev.append("")

        for i in reversed(range(len(str2))):
            cur = [""] * len(str1)
            cur.append(str2[i : ])
            for j in reversed(range(len(str1))):
                if str1[j] == str2[i]:
                    cur[j] = str1[j] + prev[j + 1]
                else:
                    string1 = str2[i] + prev[j]
                    string2 = str1[j] + cur[j + 1]
                    cur[j] = string1 if len(string1) < len(string2) else string2
            prev = cur
        return cur[0]



# MLE
# SC: O(m * n)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[""] * (len(str1) + 1) for _ in range(len(str2) + 1)]
        for i in range(len(str2)):
            dp[i][len(str1)] = str2[i : ]
        for j in range(len(str1)):
            dp[len(str2)][j] = str1[j : ]

        for i in reversed(range(len(str2))):
            for j in reversed(range(len(str1))):
                if str1[j] == str2[i]:
                    dp[i][j] = str1[j] + dp[i + 1][j + 1]
                else:
                    string1 = str2[i] + dp[i + 1][j]
                    string2 = str1[j] + dp[i][j + 1]
                    dp[i][j] = string1 if len(string1) < len(string2) else string2
        return dp[0][0]