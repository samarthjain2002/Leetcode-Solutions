"""
Accepted
1422 [Easy]
Runtime: 122 ms, faster than 5.03% of Python3 online submissions for Maximum Score After Splitting a String.
Memory Usage: 17.49 MB, less than 5.69% of Python3 online submissions for Maximum Score After Splitting a String.
"""
class Solution:
    def maxScore(self, s: str) -> int:
        sLen = len(s)
        maxScore = 0
        for split in range(1,sLen):
            zeroCount = oneCount = 0
            for left in range(split-1,-1,-1):
                if s[left] == '0':
                    zeroCount += 1
            for right in range(split,sLen):
                if s[right] == '1':
                    oneCount += 1
            maxScore = max(maxScore, zeroCount + oneCount)

        return maxScore