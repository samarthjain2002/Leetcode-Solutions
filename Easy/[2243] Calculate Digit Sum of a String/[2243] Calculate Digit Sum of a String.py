"""
Accepted
2243 [Easy]
Runtime: 20 ms, faster than 25.37% of Java online submissions for Calculate Digit Sum of a String.
Memory Usage: 13.3 MB, less than 76.12% of Java online submissions for Calculate Digit Sum of a String.
"""
class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        count = 0
        s2 = ""

        while len(s) > k:
            for i in range(0,len(s)):
                count = count + int(s[i])
                if ((i+1)%k == 0 or i == len(s)-1):
                    s2 = s2 + str(count)
                    count = 0
            s = s2
            s2 = ""

        return s