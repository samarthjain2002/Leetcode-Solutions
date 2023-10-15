#Accepted
#1404 [Medium]
#Runtime: 23 ms, faster than 53.57% of Java online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
#Memory Usage: 13.8 MB, less than 17.86% of Java online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        bits=[]
        count=len(s)-1
        count1=0
        n=0
        for _ in range(0,len(s)):
            bits.append(s[_])
        for i in range(0,len(s)):
            if(bits[i]=='1'):
                n=n+(2**count)
            else:
                pass
            count=count-1
        while(n!=1):
            if(n%2==0):
                n=n/2
            else:
                n=n+1
            count1=count1+1
        return count1