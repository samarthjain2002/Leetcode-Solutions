"""
Accepted
118 [Easy]
Runtime: 21 ms, faster than 18.43% of Python online submissions for Pascal's Triangle.
Memory Usage: 13.3 MB, less than 18.55% of Python online submissions for Pascal's Triangle.
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans=[]

        for i in range(0,numRows):
            ans.append([])
            for j in range(0,i+1):
                ans[i].append(1)

        for i in range(0,len(ans)):
            for j in range(0,len(ans[i])):
                if j==0 or i==j:
                    pass
                else:
                    ans[i][j]=ans[i-1][j-1]+ans[i-1][j]

        return ans